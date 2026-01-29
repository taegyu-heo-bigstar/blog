# Study Blog

공부한 내용이 가끔씩 기록됩니다.

## 📖 소개

이 블로그는 MkDocs Material 테마를 사용하여 학습 내용을 기록하는 개인 블로그입니다. 향후 Next.js(MDX)로 마이그레이션할 수 있도록 구조를 설계했습니다.

## 🏗️ 프로젝트 구조

```
blog/
├── docs/                     # 모든 콘텐츠 (Markdown)
│   ├── index.md              # 메인 페이지
│   ├── notes/                # 학습 노트
│   │   ├── python/           # Python 노트
│   │   ├── web/              # Web 개발 노트
│   │   └── cs/               # CS 기초 노트
│   ├── projects/             # 프로젝트 문서
│   └── references/           # 참고 자료
├── mkdocs.yml                # MkDocs 설정
├── STRUCTURE.md              # 구조 상세 문서
└── README.md                 # 이 파일
```

자세한 구조 설명은 [STRUCTURE.md](STRUCTURE.md)를 참조하세요.

## 🚀 시작하기

### 필요 조건

- Python 3.8 이상
- pip

### 설치

```bash
# Python 가상환경 생성 (선택사항이지만 권장)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 로컬 개발 서버 실행

```bash
mkdocs serve
```

브라우저에서 `http://127.0.0.1:8000`을 열어 확인할 수 있습니다.

### 빌드

```bash
mkdocs build
```

빌드된 파일은 `site/` 디렉터리에 생성됩니다.

## 📝 콘텐츠 작성

### 새 노트 추가

1. 적절한 카테고리 폴더로 이동 (예: `docs/notes/python/`)
2. 날짜 기반 파일명으로 생성: `YYYY-MM-DD-topic-name.md`
3. Frontmatter 포함:

```markdown
---
date: 2024-01-15
tags:
  - python
  - tag2
---

# 제목

내용...
```

### 카테고리

- **Notes**: 학습 내용과 기술 노트
  - Python: Python 관련 학습
  - Web: 웹 개발 관련 학습
  - CS: 컴퓨터 과학 기초
- **Projects**: 개인 프로젝트 및 실습 기록
- **References**: 참고 자료 및 치트시트

## 🔄 Next.js 마이그레이션

이 구조는 Next.js로 쉽게 마이그레이션할 수 있도록 설계되었습니다:

- **콘텐츠와 설정 분리**: `docs/` 폴더에 모든 마크다운 격리
- **명확한 폴더 구조**: URL 구조와 일치
- **일관된 Frontmatter**: 메타데이터 추출 용이
- **표준 Markdown**: MDX로 쉽게 변환

자세한 마이그레이션 가이드는 [STRUCTURE.md](STRUCTURE.md)의 "Next.js 마이그레이션 전략" 섹션을 참조하세요.

## 📚 기술 스택

- **Static Site Generator**: [MkDocs](https://www.mkdocs.org/)
- **Theme**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Content Format**: Markdown
- **Version Control**: Git & GitHub

## 📖 문서

- [STRUCTURE.md](STRUCTURE.md) - 상세 구조 및 마이그레이션 가이드
- [MkDocs 공식 문서](https://www.mkdocs.org/)
- [Material for MkDocs 문서](https://squidfunk.github.io/mkdocs-material/)

## 🤝 기여

개인 학습 블로그이지만, 제안이나 개선 사항이 있다면 이슈를 열어주세요!

## 📄 라이선스

이 프로젝트의 콘텐츠는 개인 학습 목적으로 작성되었습니다.

---

Made with ❤️ using MkDocs Material
