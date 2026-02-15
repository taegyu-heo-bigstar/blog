# Study Blog

공부한 내용이 가끔씩 기록됩니다.

<u><i>made a structure and initial content by copilot & some ai</i></u>

## 📖 소개

이 블로그는 MkDocs Material 테마를 사용하여 학습 내용을 기록하는 개인 블로그입니다. 향후 Next.js(MDX)로 마이그레이션할 수 있도록 구조를 설계했습니다.

자세한 디렉터리 구조 및 파일 명명 규칙은 [STRUCTURE.md](STRUCTURE.md)를 참조하세요.

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

새로운 노트를 작성하는 방법과 마이그레이션 전략에 대한 상세 가이드는 [STRUCTURE.md](STRUCTURE.md) 문서에서 확인할 수 있습니다.

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
