---
layout: page
title: Curriculum Vitae
subtitle: Education, appointments and professional activities.
permalink: /cv/
description: Curriculum vitae of Byounghwa Lee - education, appointments, teaching, service and awards.
---

<ul class="linkbar">
  <li><a class="primary" href="{{ site.author.cv | relative_url }}">Download full CV (PDF)</a></li>
  {% for l in site.links %}
  <li><a href="{{ l.url }}" target="_blank" rel="noopener">{{ l.name }}</a></li>
  {% endfor %}
</ul>

<ul class="toc" aria-label="Sections">
  <li><a href="#appointments">Appointments</a></li>
  <li><a href="#education">Education</a></li>
  <li><a href="#technology-transfer">Technology transfer and deployment</a></li>
  <li><a href="#patents">Patents</a></li>
  <li><a href="#presentations">Presentations</a></li>
  <li><a href="#awards">Awards</a></li>
  <li><a href="#teaching">Teaching</a></li>
  <li><a href="#selected-peer-review">Peer review</a></li>
  <li><a href="#other-activities">Other activities</a></li>
</ul>

## Appointments

<div class="rows">
  <div class="row">
    <div class="row-when">Aug 2021 – present</div>
    <div class="row-what">
      <p><strong>Senior Researcher</strong>, Electronics and Telecommunications Research Institute (ETRI)</p>
      <p class="sub">Integrated Intelligence Research Section (Jan 2024 – present) · Cyber Brain Research Section (Aug 2021 – Dec 2023)</p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Mar 2019 – Jul 2021</div>
    <div class="row-what">
      <p><strong>Staff Engineer</strong>, Samsung Research, Samsung Electronics</p>
      <p class="sub">Global AI Center, Big Data Team, Data Analytics Lab</p>
    </div>
  </div>
</div>

## Education

<div class="rows">
  <div class="row">
    <div class="row-when">Mar 2012 – Feb 2019</div>
    <div class="row-what">
      <p><strong>Ph.D. in Physics</strong>, POSTECH (integrated M.S./Ph.D. program)</p>
      <p class="sub">Statistical physics and complex systems. Advisors: Woo-Sung Jung, Hang-Hyun Jo</p>
      <p class="sub">Thesis: <em>Generative Model and Method for Correlated Bursty Dynamics</em></p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Mar 2007 – Feb 2012</div>
    <div class="row-what">
      <p><strong>B.S. in Physics</strong>, POSTECH</p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Mar 2005 – Feb 2007</div>
    <div class="row-what">
      <p><strong>Incheon Science High School</strong></p>
      <p class="sub">Graduated early after two years</p>
    </div>
  </div>
</div>

## Technology transfer and deployment {#technology-transfer}

<div class="rows">
  <div class="row">
    <div class="row-when">2026</div>
    <div class="row-what">
      <p><strong>Korean speech-based classification model for mild cognitive impairment (MCI) screening</strong>, ETRI</p>
      <p class="sub">Transferred to two companies under two technology-transfer agreements. Primary developer of the classification model and lead contributor to its field deployment (2024 – 2026); contributed to the transfer.</p>
      <p class="sub"><a href="{{ '/projects/#technology-transfer' | relative_url }}">Details under Projects</a></p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">2026</div>
    <div class="row-what">
      <p><strong>Digital-human cognitive assessment system</strong>, ETRI</p>
      <p class="sub">Developed the user interface, real-time voice and session handling and server integration for the interactive assessment system; managed system operation during field deployment.</p>
    </div>
  </div>
</div>

## Patents

Status as of September 2026. Within each section, entries are ordered by filing date, newest first
(KR filing date for patent families; US filing date for additional co-inventor applications).

<h3 class="patent-group-title">First-inventor patent families</h3>

{% assign patent_families = site.data.patents | sort: "filing_date" | reverse %}
{% for pt in patent_families %}
<article class="patent-card" aria-labelledby="patent-{{ pt.key | downcase }}">
  <header class="patent-header">
    <h4 id="patent-{{ pt.key | downcase }}">{{ pt.topic | escape }}</h4>
    <span class="patent-assignee">{{ pt.assignee | escape }}</span>
  </header>
  <div class="patent-records">
  {% include patent-record.html country="KR" title=pt.title application=pt.filed status=pt.status_text links=pt.links %}
  {%- if pt.us %}
  {% include patent-record.html country="US" title=pt.us.title application=pt.us.application publication=pt.us.publication url=pt.us.url status=pt.us.status %}
  {%- endif %}
  {%- if pt.family %}
  <p class="patent-meta patent-family">{% for f in pt.family %}{{ f | escape }}{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
  {%- endif %}
  </div>
</article>
{% endfor %}

<h3 class="patent-group-title">Additional U.S. applications as co-inventor</h3>

{% assign co_inventions = site.data.us_co_inventions | sort: "filing_date" | reverse %}
{% for pt in co_inventions %}
<article class="patent-card" aria-labelledby="co-patent-{{ forloop.index }}">
  <header class="patent-header">
    <h4 id="co-patent-{{ forloop.index }}">{{ pt.topic | escape }}</h4>
  </header>
  <div class="patent-records">
  {% include patent-record.html country="US" title=pt.title application=pt.application filing_date=pt.filing_date publication=pt.publication url=pt.url status=pt.status %}
  </div>
</article>
{% endfor %}

## Presentations

{% for g in site.data.service.presentations %}
### {{ g.group }}

<div class="rows">
  {% for p in g.items %}
  <div class="row">
    <div class="row-when">{{ p.date }}</div>
    <div class="row-what">
      <p>{{ p.title }}</p>
      <p class="sub">{{ p.venue }}{% if p.authors %} &middot; {{ p.authors }}{% endif %}</p>
    </div>
  </div>
  {% endfor %}
</div>
{% endfor %}

## Awards

<div class="rows">
  {% for a in site.data.service.awards %}
  <div class="row">
    <div class="row-when">{{ a.year }}</div>
    <div class="row-what"><p>{{ a.text }}</p></div>
  </div>
  {% endfor %}
</div>

## Teaching

<div class="rows">
  {% for t in site.data.service.teaching %}
  <div class="row">
    <div class="row-when">{{ t.term }}</div>
    <div class="row-what">
      <p>{{ t.course }}</p>
      <p class="sub">{{ t.role }}, {{ t.org }}</p>
    </div>
  </div>
  {% endfor %}
</div>

Courses I am prepared to teach, which I have not yet taught as instructor:
machine learning, deep learning and representation learning, graph and
network data analysis, and AI for science (representation and validation of
scientific data).

## Selected peer review

<div class="rows">
  {% for r in site.data.service.reviewing %}
  <div class="row">
    <div class="row-when">{{ r.years }}</div>
    <div class="row-what"><p>{{ r.journal }}</p></div>
  </div>
  {% endfor %}
</div>

## Other activities

<div class="rows">
  {% for o in site.data.service.other %}
  <div class="row">
    <div class="row-when">{{ o.year }}</div>
    <div class="row-what"><p>{{ o.text }}</p></div>
  </div>
  {% endfor %}
</div>
