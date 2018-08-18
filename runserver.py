import logging
from admin import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from admin.routes import register_blueprints

PORT: int = 5555
define('port', type=int, default=PORT)
# deploy
define('mode', default='debug')


def main():
    # 注册的路由
    register_blueprints()
    options.parse_command_line()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(options.port)
    logging.warn("[UOP] App is running on: http://localhost:%d", options.port)
    IOLoop.instance().start()

"""
if __name__ == "__main__":
    main()
"""