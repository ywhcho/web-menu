# 의약품 안전사용 전문회사 웹사이트

Django와 MySQL을 사용한 의약품 정보 제공 및 커뮤니티 웹사이트입니다.

## 주요 기능

- **회원 관리 시스템**: 회원가입, 로그인, 로그아웃, 회원정보 수정, 비밀번호 변경
- **게시판 시스템**: 게시글 작성, 조회, 수정, 삭제, 페이지네이션
- **의약정보 시스템**: 
  - 성분명/제품명 검색
  - 효능별 분류 및 필터링
  - 의약품 상세 정보 제공
- **About Us**: 회사 소개 페이지

## 기술 스택

- **Backend**: Django 6.0
- **Database**: MySQL 8.0
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Python**: 3.8+

## 설치 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd web-menu
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. MySQL 데이터베이스 설정

MySQL에 접속하여 데이터베이스를 생성합니다:

```sql
CREATE DATABASE webmenu_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. 데이터베이스 설정

`mysite/settings.py` 파일에서 데이터베이스 설정을 확인하고 필요시 수정합니다:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webmenu_db',
        'USER': 'root',
        'PASSWORD': 'your_password',  # MySQL 비밀번호로 변경
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. 마이그레이션 실행

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 8. 개발 서버 실행

```bash
python manage.py runserver
```

웹 브라우저에서 http://127.0.0.1:8000/ 으로 접속합니다.

## 관리자 페이지

http://127.0.0.1:8000/admin/ 에서 관리자 페이지에 접속할 수 있습니다.

관리자 페이지에서 다음 작업을 수행할 수 있습니다:
- 의약품 정보 등록/수정/삭제
- 게시글 관리
- 사용자 관리

## 샘플 데이터 생성 (선택사항)

Django shell을 사용하여 샘플 데이터를 생성할 수 있습니다:

```bash
python manage.py shell
```

```python
from medicine.models import Medicine
from board.models import Post
from django.contrib.auth.models import User

# 의약품 샘플 데이터
Medicine.objects.create(
    product_name='타이레놀',
    ingredient_name='아세트아미노펜',
    efficacy='antipyretic',
    dosage='성인 1회 1-2정, 1일 3-4회 복용',
    manufacturer='한국존슨앤드존슨',
    precautions='간 질환 환자는 주의하여 복용하십시오.'
)

# 게시글 샘플 데이터 (관리자 계정 필요)
user = User.objects.first()
Post.objects.create(
    title='의약품 안전사용 가이드',
    content='의약품을 안전하게 사용하는 방법에 대해 알아봅시다.',
    author=user
)
```

## URL 구조

- `/` - 메인 페이지
- `/about/` - About Us
- `/accounts/signup/` - 회원가입
- `/accounts/login/` - 로그인
- `/accounts/logout/` - 로그아웃
- `/accounts/profile/edit/` - 회원정보 수정
- `/accounts/password/change/` - 비밀번호 변경
- `/board/` - 게시판 목록
- `/board/create/` - 게시글 작성
- `/board/<int:pk>/` - 게시글 상세
- `/board/<int:pk>/edit/` - 게시글 수정
- `/board/<int:pk>/delete/` - 게시글 삭제
- `/medicine/` - 의약정보 메인
- `/medicine/search/` - 의약품 검색
- `/medicine/efficacy/` - 효능별 보기
- `/medicine/<int:pk>/` - 의약품 상세정보

## 프로젝트 구조

```
web-menu/
├── manage.py
├── requirements.txt
├── README.md
├── mysite/              # 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── accounts/            # 회원 관리 앱
├── board/               # 게시판 앱
├── medicine/            # 의약정보 앱
├── static/              # 정적 파일
│   └── css/
│       └── style.css
└── templates/           # 템플릿 파일
    ├── base.html
    ├── index.html
    ├── about.html
    ├── accounts/
    ├── board/
    └── medicine/
```

## 보안 사항

- CSRF 보호 활성화
- 비밀번호 암호화 저장 (Django 기본)
- SQL Injection 방지 (Django ORM)
- 로그인 필수 페이지 접근 제어
- 게시글 수정/삭제 권한 검증

## 라이선스

MIT License

## 문의

기술 지원이 필요한 경우 이슈를 등록해주세요.

