# 프로젝트 구조 완성 요약

## 📁 1. 디렉터리 트리

```
blog/
├── README.md                              # 프로젝트 소개 및 사용 가이드
├── STRUCTURE.md                           # 상세 구조 및 마이그레이션 가이드
├── requirements.txt                       # Python 의존성 (mkdocs-material)
├── mkdocs.yml                            # MkDocs 설정 파일 (Material 테마)
├── .gitignore                            # Git 무시 파일
│
└── docs/                                 # 모든 콘텐츠 (Markdown)
    ├── index.md                          # 메인 홈페이지
    │
    ├── notes/                            # 📚 학습 노트 카테고리
    │   └── subject/               # 특정 분야 관련 노트
    │       ├── index.md
    │       └── YYYY-MM-DD-topic.md
    ├── projects/                  # 프로젝트 문서
    │   ├── index.md
    │   └── YYYY-MM-project-name.md
    └── references/                # 참고 자료
        ├── index.md
        └── topic-name.md
```

## 📄 2. mkdocs.yml 예시 (핵심 부분)

```yaml
# 사이트 정보
site_name: Study Blog
site_description: 공부한 내용이 가끔씩 기록됩니다
site_author: Taegyu Heo

# Material 테마 설정
theme:
  name: material
  language: ko
  palette:
    # 라이트/다크 모드 지원
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
  
  features:
    - navigation.instant        # 빠른 페이지 로딩
    - navigation.tabs           # 네비게이션 탭
    - navigation.sections       # 섹션 구분
    - search.suggest            # 검색 제안
    - content.code.copy         # 코드 복사 버튼

# 네비게이션 구조
nav:
  - Home: index.md
  - Notes:
    - notes/index.md
    - os:
      - notes/os/index.md
    - algorithm:
      - notes/algorithm/index.md
    - c:
      - notes/c/index.md
  - Projects:
    - projects/index.md
  - References:
    - references/index.md

# Markdown 확장 기능
markdown_extensions:
  - admonition                  # 경고/정보 박스
  - toc:
      permalink: true           # 헤딩 링크
  - pymdownx.highlight          # 코드 하이라이팅
  - pymdownx.superfences        # 코드 블록 (Mermaid 지원)
  - pymdownx.tabbed             # 탭
  - pymdownx.tasklist           # 체크리스트

# 플러그인
plugins:
  - search:                     # 검색 (한국어/영어)
      lang:
        - ko
        - en
  - tags                        # 태그 시스템
```

## 📝 3. index.md 템플릿 예시

### 메인 index.md (docs/index.md)

```markdown
# Welcome to My Study Blog

공부한 내용이 가끔씩 기록됩니다.

## 📚 About
이 블로그는 개인 학습 내용을 정리하고 공유하기 위한 공간입니다.

## 🗂️ Categories

### [Notes](/notes/)
학습 내용과 기술 노트
- [algorithm](/notes/algorithm/)
- [os](/notes/os/)
- [c](/notes/c/)

### [Projects](/projects/)
개인 프로젝트 및 실습 기록

### [References](/references/)
참고 자료 및 유용한 링크 모음
```

### 카테고리 index.md (docs/notes/python/index.md)

```markdown
# Python Notes

Python 프로그래밍 언어 관련 학습 내용을 정리합니다.

## 📚 Topics
- 기본 문법 및 개념
- 표준 라이브러리
- 웹 프레임워크 (Django, Flask, FastAPI)
- 데이터 분석 (NumPy, Pandas)

## 📝 Notes
새로운 노트를 추가하려면, 날짜 기반 파일명을 사용하세요:
`YYYY-MM-DD-topic-name.md`

## 🔗 Useful Resources
- [Python 공식 문서](https://docs.python.org/)
```

### 콘텐츠 파일 템플릿 (with Frontmatter)

```markdown
---
date: 2024-01-15
updated: 2024-01-15
tags:
  - python
  - decorators
  - advanced
---

# Python 데코레이터 이해하기

데코레이터는 함수를 수정하지 않고 기능을 확장하는 Python의 강력한 기능입니다.

## 기본 개념

\```python
def my_decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
\```

## 참고 자료
- [Python 공식 문서](https://docs.python.org/)

---

[← Back to Python Notes](/notes/python/)
```

## 🚀 4. 사용 방법

### 설치 및 실행

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 로컬 개발 서버 실행
mkdocs serve
# → http://127.0.0.1:8000 에서 확인

# 3. 빌드
mkdocs build
# → site/ 폴더에 정적 HTML 생성

# 4. GitHub Pages 배포
mkdocs gh-deploy
```

### 새 콘텐츠 추가

```bash
# 1. 날짜 기반 파일 생성
touch docs/notes/python/2024-01-30-new-topic.md

# 2. Frontmatter와 내용 작성
# 3. mkdocs serve로 확인
# 4. Git commit & push
```

## 🔄 5. Next.js 마이그레이션 준비 완료

### 현재 구조의 장점

✅ **콘텐츠와 설정 완전 분리**
- `docs/` 폴더에 모든 Markdown 격리
- `mkdocs.yml`에 설정만 분리

✅ **명확한 폴더 구조**
- URL 구조와 1:1 매핑
- `/notes/python/` → `docs/notes/python/`

✅ **일관된 메타데이터**
- YAML Frontmatter 표준 사용
- Next.js의 gray-matter와 호환

✅ **표준 Markdown**
- MDX로 쉽게 변환 가능
- React 컴포넌트 임베드 가능

### Next.js 마이그레이션 시 변경 사항

```
MkDocs 구조                Next.js App Router 구조
──────────────────────────────────────────────────
docs/                  →   app/ (or content/)
  index.md             →     page.tsx
  notes/               →     notes/
    python/            →       python/ for your repository, organization, or user account.


      index.md         →         page.tsx
      2024-01-15-*.md  →         [slug]/page.mdx
```

## 📊 6. 주요 기능

### Material 테마 기능
- ✅ 반응형 디자인
- ✅ 다크/라이트 모드
- ✅ 검색 기능 (한국어/영어)
- ✅ 네비게이션 탭
- ✅ 코드 하이라이팅
- ✅ 코드 복사 버튼
- ✅ 태그 시스템

### Markdown 확장
- ✅ Admonitions (경고/정보 박스)
- ✅ 코드 블록 (문법 강조)
- ✅ 표 지원
- ✅ 각주
- ✅ 체크리스트
- ✅ Mermaid 다이어그램
- ✅ 수학 표기 (LaTeX)

## 📚 7. 문서 참조

- **README.md**: 프로젝트 소개 및 빠른 시작 가이드
- **STRUCTURE.md**: 상세 구조 설명 및 Next.js 마이그레이션 가이드
- **mkdocs.yml**: 전체 설정 파일 (주석 포함)
- **각 index.md**: 카테고리별 가이드 및 예제

## ✅ 8. 완성된 항목

1. ✅ 디렉터리 구조 설계 및 생성
2. ✅ mkdocs.yml 완전 설정 (Material 테마)
3. ✅ 모든 index.md 파일 생성 (메인 + 모든 카테고리)
4. ✅ 예제 콘텐츠 파일 3개 (Python, Web, CS)
5. ✅ 날짜 기반 파일명 규칙 적용
6. ✅ Frontmatter 템플릿 정의
7. ✅ .gitignore 추가 (빌드 아티팩트 제외)
8. ✅ requirements.txt 추가
9. ✅ README.md 업데이트
10. ✅ STRUCTURE.md 작성 (마이그레이션 가이드)
11. ✅ MkDocs 빌드 테스트 성공

## 🎯 다음 단계 (선택사항)

사용자가 원하는 경우 추가할 수 있는 항목들:

- GitHub Actions 워크플로우 (자동 배포)
- 커스텀 CSS/JS (브랜딩)
- Google Analytics 연동
- 댓글 시스템 (Giscus 등)
- RSS 피드
- 사이트맵 최적화
