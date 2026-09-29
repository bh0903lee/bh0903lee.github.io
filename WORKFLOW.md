# 홈페이지 작업·GitHub 반영 순서

이 저장소(bh0903lee.github.io)는 GitHub Pages로 자동 배포된다. `main`에 push하면 1~2분 뒤 https://bh0903lee.github.io 에 반영된다.
PC와 노트북 어느 쪽에서 작업하든 **아래 순서를 GitHub 반영 전에 한 번 훑는다.**

## 0. 전제

- GitHub가 중앙 사본이다. 각 PC의 폴더는 마지막 pull/push 시점에 멈춰 있고 **자동으로 갱신되지 않는다.**
- 노트북: `~/Downloads/bh0903lee.github.io-main` (2026-09-29에 정식 클론으로 교체). 커밋 작성자와 인증은 저장소 로컬 설정에 들어 있어 `git pull`·`git push`가 바로 된다.
- 원래 PC: 예전에 push하던 폴더 그대로. 처음 다시 쓸 때 `git pull`부터 한다.
- 인증 토큰(PAT)·로컬 경로·편집 메모는 이 저장소에 올리지 않는다(`.gitignore`의 DEPLOY.md, NOTES.md, `*.local.md` 참고).

## 1. 작업 시작 전

```
git pull
```

다른 PC에서 올린 변경을 먼저 받는다. 이걸 빼먹고 수정하면 push가 거부된다(아래 5번).

## 2. 수정 후 정적 검사

```
python tools/check.py
```

PyYAML이 필요하다(없으면 `pip install pyyaml` 또는 venv). YAML 문법, **중복 키**, Liquid 태그 짝, include·에셋·탐색 링크를 확인한다. `All checks passed.`가 나와야 한다.

## 3. 로컬 빌드(선택)

GitHub Pages가 알아서 빌드하므로 필수는 아니다. 화면을 미리 보려면:

```
bundle install            # 처음 한 번. Gemfile은 GitHub Pages와 같은 버전
bundle exec jekyll serve  # http://127.0.0.1:4000
```

- Ruby 3.2 이상에서는 github-pages가 고정한 liquid 4.0.3이 `tainted?` 오류를 낸다. `String#tainted?`를 `false`로 돌려주는 보정 파일을 `RUBYOPT=-r<파일>`로 끼우면 된다. Ruby 3.4 이상은 `csv`, `base64`, `bigdecimal` gem도 따로 필요하다.
- `vendor/`, `.bundle/`, `Gemfile.lock`, `_site/`는 저장소에 올리지 않는다(gem은 저장소 밖 경로에 설치).

## 4. 반영 전 체크리스트

- [ ] 1번 `git pull`을 했다.
- [ ] 2번 `tools/check.py`가 통과했다.
- [ ] 역할 표현: "Primary developer", "field deployment" (CV PDF와 동일). "Lead developer", "field trials"는 쓰지 않는다.
- [ ] 기술이전·앱·실증에 **업체명, 계약금액, 실증 장소**를 쓰지 않는다.
- [ ] 논문 **정확도 수치**를 홈페이지에 쓰지 않는다(정성 문장만).
- [ ] 없는 경험(멘토링·세미나·공동지도·과제책임자)을 만들지 않는다. "강의 가능 분야" 문단은 교수 지원 서류용이며 홈페이지에는 넣지 않는다.
- [ ] 진행 중 연구는 "ongoing / under review"로만 표기하고 출판 성과처럼 쓰지 않는다.
- [ ] 파비콘은 중립 문양을 유지한다(이니셜 사용 안 함).
- [ ] 웹 CV와 PDF CV의 날짜·경력·특허 상태가 어긋나지 않는다.
- [ ] `git status`에 올리면 안 되는 파일(gem, 빌드 산출물, 메모)이 없다.

## 5. 반영

```
git status
git add -A
git commit -m "무엇을 왜 바꿨는지 한 줄"
git push
```

1~2분 뒤 https://bh0903lee.github.io 에서 바뀐 페이지를 직접 확인한다. 파비콘은 브라우저 캐시 때문에 늦게 바뀔 수 있다.

**push가 거부되면(`rejected`, `non-fast-forward`)**: 다른 PC의 커밋이 먼저 올라간 것이다.

```
git pull
# 충돌(CONFLICT)이 나면 해당 파일을 열어 <<<<<<< ======= >>>>>>> 표시를 정리한 뒤
git add -A
git commit
git push
```

## 6. 자주 쓰는 확인 명령

```
git status          # 바뀐 파일
git log --oneline -5  # 최근 커밋
git diff            # 아직 커밋하지 않은 변경 내용
```
