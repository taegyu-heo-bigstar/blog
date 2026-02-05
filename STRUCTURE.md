# Directory Structure Documentation

## 📁 프로젝트 구조

이 문서는 MkDocs 블로그의 디렉터리 구조와 Next.js로의 마이그레이션 전략을 설명합니다.

## 디렉터리 트리
## 디렉터리 트리
## 디렉터리 트리

```
blog/
├── docs/                          # 모든 콘텐츠 파일 (Markdown)
│   ├── index.md                   # 메인 홈페이지
│   ├── notes/                     # 학습 노트 카테고리
│   │   ├── index.md               # Notes 인덱스
│   │   └── subject/               # 특정 분야 관련 노트
│   │   └── subject/               # 특정 분야 관련 노트
│   │   └── subject/               # 특정 분야 관련 노트
│   │   └── subject/               # 특정 분야 관련 노트
│   │   └── subject/               # 특정 분야 관련 노트
│   │       ├── index.md
│   │       └── YYYY-MM-DD-topic.md
│   ├── projects/                  # 프로젝트 문서
│   │   ├── index.md
│   │   └── YYYY-MM-project-name.md
│   └── references/                # 참고 자료
│       ├── index.md
│       └── topic-name.md
├── mkdocs.yml                     # MkDocs 설정 파일
├── .gitignore                     # Git 무시 파일
└── README.md                      # 프로젝트 설명
```

## 📝 파일 명명 규칙

### 날짜 기반 파일 (Notes, Projects)

```
YYYY-MM-DD-topic-name.md
```

**예시:**
- `2024-01-15-decorators.md`
- `2024-01-20-react-hooks.md`
- `2024-01-25-binary-tree-traversal.md`

### 주제 기반 파일 (References)

```
topic-name.md
```

**예시:**---
date: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag1
  - tag2
  - tag3
status: [optional: draft|published|archived]
---

# 제목

내용...
**예시:**---
date: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag1
  - tag2
  - tag3
status: [optional: draft|published|archived]
---

# 제목

내용...
- `python-quick-reference.md`
- `git-cheatsheet.md`
- `web-dev-tools.md`

## 🎯 콘텐츠 작성 가이드

### Frontmatter 구조

모든 콘텐츠 파일은 YAML frontmatter로 시작합니다:

```markdown
------
date: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag1
  - tag2
  - tag3
status: [optional: draft|published|archived]
---

# 제목

내용...
------
date: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag1
  - tag2
  - tag3
status: [optional: draft|published|archived]
---

# 제목

내용...
date: YYYY-MM-DD
updated: YYYY-MM-DD
updated: YYYY-MM-DD
updated: YYYY-MM-DD
updated: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag1
  - tag2
  - tag3
status: [optional: draft|published|archived]
---

# 제목

내용...
```

### 카테고리별 템플릿

#### Notes 템플릿

```markdown
---
date: 2024-01-15
tags:
  - python
  - advanced
---

# 제목

간단한 소개

## 섹션 1

내용...

## 예제 코드

\```python
# 코드 예제
\```

## 참고 자료

- [링크1](url)
- [링크2](url)

---

[← Back to Category](/notes/category/)
```

#### Projects 템플릿

```markdown
---
date: 2024-01-15
status: completed
tags:
  - react
  - typescript
---

# 프로젝트 이름

## Overview
프로젝트 개요

## Tech Stack
- React
- TypeScript
- Next.js

## Features
- 기능 1
- 기능 2

## Challenges & Solutions
직면한 문제와 해결 방법

## Lessons Learned
배운 점

## Links
- [GitHub](url)
- [Demo](url)
```

## 🔄 Next.js 마이그레이션 전략

### 현재 구조의 장점

1. **콘텐츠와 설정 분리**: `docs/` 폴더에 모든 마크다운 파일이 격리됨
2. **명확한 카테고리**: 폴더 구조가 URL 구조와 일치
3. **일관된 Frontmatter**: 메타데이터 추출이 용이
4. **표준 Markdown**: MDX로 쉽게 변환 가능

### Next.js App Router 구조로의 매핑

```
MkDocs 구조              →  Next.js 구조
─────────────────────────────────────────────────────
docs/                    →  app/
  index.md               →    page.tsx (or page.mdx)
  notes/                 →    notes/
    index.md             →      page.tsx
    python/              →      python/
      index.md           →        page.tsx
      2024-01-15-*.md    →        [slug]/page.mdx
```

### 마이그레이션 체크리스트

- [ ] **Step 1: 콘텐츠 유지**
  - `docs/` 폴더를 `content/` 또는 `posts/`로 이름 변경
  - Frontmatter 형식 유지 (호환됨)

- [ ] **Step 2: MDX 변환**
  - `.md` 파일을 `.mdx`로 변경
  - 필요시 React 컴포넌트 임베드

- [ ] **Step 3: 라우팅 구조**
  - Next.js App Router에 맞게 폴더 구조 조정
  - 동적 라우트 생성 (`[slug]` 폴더)

- [ ] **Step 4: 메타데이터 처리**
  - Frontmatter 파싱 (gray-matter 라이브러리)
  - Next.js Metadata API 사용

- [ ] **Step 5: UI 컴포넌트**
  - MkDocs Material 테마를 참고하여 React 컴포넌트 작성
  - 네비게이션, 검색, TOC 구현

### 추천 Next.js 라이브러리

```json
{
  "dependencies": {
    "next": "^15.0.0",
    "react": "^18.0.0",
    "next-mdx-remote": "^5.0.0",
    "gray-matter": "^4.0.3",
    "remark": "^15.0.0",
    "remark-gfm": "^4.0.0",
    "rehype-pretty-code": "^0.10.0",
    "contentlayer": "^0.3.4"
  }
}
```

### 예시: Next.js에서 마크다운 로딩

```typescript
// lib/posts.ts
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const contentDirectory = path.join(process.cwd(), 'content');

export function getAllPosts() {
  const fileNames = fs.readdirSync(contentDirectory);
  const allPostsData = fileNames.map((fileName) => {
    const slug = fileName.replace(/\.mdx?$/, '');
    const fullPath = path.join(contentDirectory, fileName);
    const fileContents = fs.readFileSync(fullPath, 'utf8');
    const { data, content } = matter(fileContents);

    return {
      slug,
      content,
      ...data,
    };
  });

  return allPostsData;
}
```

## 🚀 로컬 개발 환경

### MkDocs 설치 및 실행

```bash
# Python 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# MkDocs 및 플러그인 설치
pip install -r requirements.txt

# 로컬 서버 실행
mkdocs serve

# 빌드
mkdocs build
```

### 배포

```bash
# GitHub Pages 배포
mkdocs gh-deploy
```

## 📚 참고 자료

### MkDocs
- [MkDocs 공식 문서](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

### Next.js
- [Next.js 공식 문서](https://nextjs.org/docs)
- [MDX 공식 문서](https://mdxjs.com/)
- [Contentlayer](https://contentlayer.dev/)

---
