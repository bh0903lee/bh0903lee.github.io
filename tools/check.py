"""Static checks for this site: YAML validity, Liquid block balance,
include/layout resolution, and asset references. Needs only PyYAML, no Ruby.

Run it after editing anything in _data/ or _config.yml:

    python tools/check.py
"""
import os, re, sys, glob
import yaml

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings = [], []

# Markdown files that document the repo rather than being pages of the site.
REPO_DOCS = {"README.md", "DEPLOY.md"}

BLOCK_TAGS = {"if", "unless", "for", "case", "capture", "raw", "comment", "tablerow"}
MID_TAGS = {"else", "elsif", "when", "break", "continue"}


def split_front_matter(text, path):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        errors.append(f"{path}: front matter opened but never closed")
        return None, text
    fm_raw = text[3:end]
    body = text[end + 4:]
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid front-matter YAML -> {e}")
        fm = {}
    return fm, body


def check_liquid(text, path):
    stack = []
    for m in re.finditer(r"\{%-?\s*(\w+)", text):
        tag = m.group(1)
        line = text.count("\n", 0, m.start()) + 1
        if tag in BLOCK_TAGS:
            stack.append((tag, line))
        elif tag.startswith("end"):
            want = tag[3:]
            if not stack:
                errors.append(f"{path}:{line}: {{% {tag} %}} with no open block")
            elif stack[-1][0] != want:
                errors.append(
                    f"{path}:{line}: {{% {tag} %}} closes {{% {stack[-1][0]} %}} "
                    f"opened at line {stack[-1][1]}")
                stack.pop()
            else:
                stack.pop()
        elif tag in MID_TAGS and not stack:
            errors.append(f"{path}:{line}: {{% {tag} %}} outside any block")
    for tag, line in stack:
        errors.append(f"{path}:{line}: {{% {tag} %}} is never closed")

    # unbalanced delimiters
    if text.count("{%") != text.count("%}"):
        errors.append(f"{path}: unbalanced {{% ... %}} delimiters")
    if text.count("{{") != text.count("}}"):
        errors.append(f"{path}: unbalanced {{{{ ... }}}} delimiters")


def rel(p):
    return os.path.relpath(p, SITE).replace("\\", "/")


# --- config -----------------------------------------------------------------
cfg_path = os.path.join(SITE, "_config.yml")
try:
    cfg = yaml.safe_load(open(cfg_path, encoding="utf-8"))
    print("OK  _config.yml parses")
except yaml.YAMLError as e:
    errors.append(f"_config.yml: {e}")
    cfg = {}

# --- data files -------------------------------------------------------------
data = {}
for f in sorted(glob.glob(os.path.join(SITE, "_data", "*.yml"))):
    try:
        data[os.path.basename(f)[:-4]] = yaml.safe_load(open(f, encoding="utf-8"))
        print(f"OK  _data/{os.path.basename(f)} parses")
    except yaml.YAMLError as e:
        errors.append(f"_data/{os.path.basename(f)}: {e}")

# --- templates and pages ----------------------------------------------------
targets = []
for pat in ("*.md", "_layouts/*.html", "_includes/*.html"):
    targets += glob.glob(os.path.join(SITE, pat))

layouts = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(SITE, "_layouts", "*.html"))}
includes = {os.path.basename(p) for p in glob.glob(os.path.join(SITE, "_includes", "*.html"))}

for path in sorted(targets):
    name = rel(path)
    if name in REPO_DOCS:
        continue
    text = open(path, encoding="utf-8").read()
    fm, body = split_front_matter(text, name)
    check_liquid(body if fm is not None else text, name)

    if fm:
        lay = fm.get("layout")
        if lay and lay not in layouts:
            errors.append(f"{name}: layout '{lay}' not found in _layouts/")
    elif name.endswith(".md"):
        errors.append(f"{name}: page has no front matter, Jekyll will not render it")

    for m in re.finditer(r"\{%-?\s*include\s+([\w./-]+)", text):
        if m.group(1) not in includes:
            errors.append(f"{name}: include '{m.group(1)}' not found in _includes/")

    # referenced local assets
    for m in re.finditer(r"['\"](/assets/[\w./-]+)['\"]", text):
        if not os.path.exists(os.path.join(SITE, m.group(1).lstrip("/"))):
            errors.append(f"{name}: missing asset {m.group(1)}")

print(f"OK  scanned {len(targets)} template/page files")

# --- config-referenced assets ----------------------------------------------
for key in ("photo", "cv"):
    v = (cfg.get("author") or {}).get(key)
    if v and not os.path.exists(os.path.join(SITE, v.lstrip("/"))):
        errors.append(f"_config.yml: author.{key} -> {v} does not exist")

# --- nav targets exist ------------------------------------------------------
perms = {}
for p in glob.glob(os.path.join(SITE, "*.md")):
    if os.path.basename(p) in REPO_DOCS:
        continue
    fm, _ = split_front_matter(open(p, encoding="utf-8").read(), rel(p))
    if fm and fm.get("permalink"):
        perms[fm["permalink"]] = rel(p)
for item in cfg.get("nav", []):
    if item["url"] not in perms:
        errors.append(f"_config.yml: nav '{item['title']}' -> {item['url']} has no page")
print(f"OK  {len(perms)} pages: " + ", ".join(sorted(perms)))

# --- publication sanity -----------------------------------------------------
pubs = data.get("publications", [])
aliases = set((cfg.get("author") or {}).get("aliases", []))
seen = set()
for p in pubs:
    for field in ("title", "authors", "venue", "year", "date"):
        if not p.get(field):
            errors.append(f"publications {p.get('key', '?')}: missing '{field}'")
    if p.get("key") in seen:
        errors.append(f"publications: duplicate key {p['key']}")
    seen.add(p.get("key"))
    if not (aliases & set(p.get("authors") or [])):
        warnings.append(f"publications {p.get('key')}: no author matches an alias, "
                        f"name will not be bolded")
    if p.get("date") and p.get("year") and p["date"].year != p["year"]:
        errors.append(f"publications {p['key']}: year {p['year']} != date {p['date']}")
print(f"OK  {len(pubs)} publications checked")

for name, required in (("patents", ("title", "status", "status_text")),
                       ("projects", ("name", "org", "period", "role"))):
    for item in data.get(name, []):
        for field in required:
            if not item.get(field):
                errors.append(f"{name}: entry missing '{field}' -> {item.get('title') or item.get('name')}")
    print(f"OK  {len(data.get(name, []))} {name} checked")

# --- report -----------------------------------------------------------------
print()
for w in warnings:
    print("WARN", w)
if errors:
    print()
    for e in errors:
        print("FAIL", e)
    sys.exit(1)
print("All checks passed.")
