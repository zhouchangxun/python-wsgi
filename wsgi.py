# server.py

from wsgiref.simple_server import make_server


# from hello import application

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


httpd = make_server('', 3000, application)
print "Serving HTTP on port 3000..."

httpd.serve_forever()
