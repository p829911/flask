from flask import Flask
from flask import g
from flask import Response
from flask import make_response
from flask import request
from datetime import datetime, date

app = Flask(__name__)
app.debug = True


@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response('SET COOKIE')
    res.set_cookie(key, val)
    return make_response(res)


@app.route('/rc')
def rc():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return 'cookie[' + key + '] = ' + val


@app.route('/reqenv')
def reqenv():
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


def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans


@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return '우리나라 시간 형식: ' + str(datestr)


@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')
    return "q= %s" % str(q)
# args get, form get, values: URL localhost:5000/rp?q=123
# args.getlist: URL localhost:5000/rp?q=123&q=456

# @app.before_request
# def before_request():
#     print('before_request!!!')
#     g.str = '한글'


@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)


@app.route('/gg')
def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', '111')


@app.route('/res1')
def res1():
    custom_res = Response('Custom Response', 200, {'test': 'ttt'})
    return make_response(custom_res)


@app.route('/')
def helloworld():
    return "Hello Flask World!"
