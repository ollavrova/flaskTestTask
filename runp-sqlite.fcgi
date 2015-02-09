from flipflop import WSGIServer
from library import app

if __name__ == '__main__':
    WSGIServer(app).run()
