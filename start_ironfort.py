from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from .TuShare.wsgi import application
host = "127.0.0.1"
port = 9000
print('TuShare is running ............')
ws_server = WSGIServer(
    (host,port),
    application,
    log=None,
    handler_class=WebSocketHandler
)

try:
    ws_server.serve_forever()
except KeyboardInterrupt:
    print('服务器关闭.......')
    pass