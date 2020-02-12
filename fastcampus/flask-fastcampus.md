## FLASK

- FASTCAMPUS 풀스택 강의

#### 플라스크 소개

프레임워크

1. 자주 사용되는 코드를 체계화하여 쉽게 사용할 수 있도록 도와주는 코드 집합
2. 라이브러리와 혼동될 수 있지만 좀 더 규모가 크고 프로젝트의 기반이 됨
3. 건축에 비유하면 구조를 만드는 골조가 프레임워크라면 그 외 자재들이 라이브러리가 됨

소규모 프로젝트 (작고, 간단간단하게 만들 수 있다) - 챗봇

#### MVC 패턴

MVC는 디자인 패턴 중 하나

- **Model**: 데이터베이스와 연결되는 부분

- **View**: 클라이언트가 보는 부분

- **Controller**: 접근 URL에 따라 비즈니스 로직이 수행되는 부분

![](https://user-images.githubusercontent.com/17154958/73512400-ce61ff00-442c-11ea-8dd1-c28d18356279.png)

#### SQLAlchemy 소개

**app.py**

```python
pip install flask-sqlalchemy

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Test(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

db.create_all()

@app.route('/')
def hello():
    return 'Hello world!'

```

```bash
sqlite3 db.sqlite
.tables
.schema
```



COMMIT: 반영하지 못한 것들을 실제로 반영하는 역할

TEARDOWN: 사용자가 웹사이트에 요청을 하고, 작업이 끝나면 나오는 것



#### Jinja2 소개

```python
from flask import render_template

@app.route('/')
def hello():
    return render_template('hello.html')
```

```bash
FLASK_APP=app.py flask run
```

flask 안에서 내부적으로 jinja를 사용하고 있다.



#### 모델 만들기, 회원

CRUD: 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제) 를 묶어서 일컫는 말이다. 사용자 인터페이스가 갖추어야 할 기능 (정보의 참조/검색/갱신)을 가리키는 용어로서도 사용된다.

**app.py**

```python
import os
from flask import Flask
from flask import render_template
from models import db

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) # db안에 config 설정 초기화
    db.app = app # db에 app 넣어주기
    db.create_all() # db 생성

    app.run(host='127.0.0.1', port=5000, debug=True)
  
```



**models.py**

```python
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

```



**hello.html**

```html
Hello World!
```



#### 뷰 만들기, 회원

bootstrap

**register.html**

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0 shrink-to-fit=no">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
    </script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
    </script>
</head>

<body>
    <div class="container">
        <div class="row mt-5">
            <h1>회원가입</h1>
        </div>
        <div class="row mt-5">
            <div class="col-12">
                <form method="POST">
                    <div class="form-group">
                        <label for="username">아이디</label>
                        <input type="text" class="form-control" id="userid" placeholder="아이디"" name=" userid" />
                    </div>
                    <div class="form-group">
                        <label for="username">사용자 이름</label>
                        <input type="text" class="form-control" id="username" placeholder="사용자 이름" name="username" />
                    </div>
                    <div class="form-group">
                        <label for="password">패스워드</label>
                        <input type="password" class="form-control" id="password" placeholder="비밀번호"" name="
                            password" />
                    </div>
                    <div class="form-group">
                        <label for="re-password">비밀번호 확인</label>
                        <input type="password" class="form-control" id="re-password" placeholder="비밀번호 확인"
                            name="re-password" />
                    </div>
                    <button type="summit" class="btn btn-primary">등록</button>
                </form>
            </div>
        </div>
    </div>
</body>

</html>
```



#### 컨트롤러 만들기, 회원



#### Flask-WTF

**csrf** 방지

사이트 간 요청 위조 (Cross-site request forgery, CSRF)는 웹사이트 취약점 공격의 하나로, 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 하는 공격을 말한다.

#### static file 관리

프로젝트 안에다가 static 폴더를 만들면 끝이다.