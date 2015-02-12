# -*- coding: utf-8 -*-
from app import create_app
from flask.ext.babel import Babel, lazy_gettext
from flask.ext.login import LoginManager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy


app = create_app()

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

babel = Babel(app)
babel.init_app(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
lm.login_message = lazy_gettext('Please log in to access this page.')

from .views import *
from .models import *