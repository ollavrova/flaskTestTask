# # -*- coding: utf-8 -*-
from library import create_app
import os
import sys
from config import PROJECT_DIR

activate_this = os.path.join(PROJECT_DIR, 'venv', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)

app = create_app()
# from flipflop import WSGIServer


if __name__ == '__main__':
    # WSGIServer(app).run()
    app.run()

from library.app import app as application