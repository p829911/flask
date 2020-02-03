# FLASK

- 유튜브 시니어코딩IndiFlex 강의

### Flask Request Event Handler

```python
@app.before_first_request
def ...
```

사용자가 서버에 요청을 보낸다. 첫번째 요청을 보낼때 이 함수를 무조건 실행 시켜라

```python
@app.before_request
def ...
```

매번 요청할 때 이 함수를 실행시켜라 (Web Filter)

```python
@app.after_request
def ...(response)
```

요청을 다 처리했을 때 실행시켜라

ex) db 커넥션 close

```python
@app.teardown_request
def ...(exception)
```

teardown == destroy

stream 다 내려가고 나서 띄우는것

```python
@app.teardown_appcontext
def ...(exception)
```

appcontext == application context

application context가 끝났을 때



### Routing

```python
@app.route('/test')
def ...
```

 

```python
@app.route('/test', method=['POST', 'PUT'])
def ...
```



```python
@app.route('/test/<tid>')
def test3(tid):
	print('tid is', tid)
```



```python
@app.route('/test', defaults={'page': 'index'})
@app.route('/test/<page>')
def xxx(page):
```



```python
@app.route('/test', host='abc.com')
@app.route('/test', redirect_to='/new_test')
```



### Routing (Cont'd): Subdomain

```python
app.config['SERVER_NAME'] = 'local.com:5000'

@app.route('/')
def helloworld_local():
return 'Hello Local.com!'

@app.route('/', subdomain='g')
def helloworld():
	return 'Hello G.Local.com!!!'
```

www.naver.com

blog.naver.com (blog 부분이 subdomain이다.)



### Request Parameter

```python
# MultiDict Type
...get('<param name>', <default-value>, <type>)
methods: get, getlist, clear, etc
   
# GET 
request.args.get('q')

# POST
request.form.get('p', 123)

# GET or POST
request.values.get('v')

# Parameters
request.args.getlist('qs')
```



### Request.environ

```python
return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
        'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
        'PATH_INFO: %(PATH_INFO) s <br>'
        'QUERY_STRING: %(QUERY_STRING) s <br>'
        'SERVER_NAME: %(SERVER_NAME) s <br>'
        'SERVER_PORT: %(SERVER_PORT) s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
        'wsgi.version: %(wsgi.version) s <br>'
        'wsgi.url_scheme: %(wsgi.input) s <br>'
        'wsgi.input: %(wsgi.input) s <br>'
        'wsgi.errors: %(wsgi.errors) s <br>'
        'wsgi.multithread: %(wsgi.multithread) s <br>'
        'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
        'wsgi.run_once: %(wsgi.run_once) s') % request.environ
```



### Request

XHR (XMLHttpRequest) : AJAX 요청을 생성하는 JavaScript API 이다. XHR의 메서드로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다.

```python
request.is_xhr
request.endpoint
request.get_json()

app.config.update(MAX_CONTENT_LENGTH=1024*1024)
request.max_content_length
```

