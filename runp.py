# # -*- coding: utf-8 -*-
import os
import sys
from flask.ext.babel import Babel

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

if not (PROJECT_DIR in sys.path):
    sys.path.append(PROJECT_DIR)

from library import create_app
app = create_app()
app.config.from_object('config')
babel = Babel(app)

from library.views import *
from library.models import *

if __name__ == '__main__':
    babel.init_app(app)
    app.run()

from library import app as application

