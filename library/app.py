# -*- coding: utf-8 -*-
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import render_template, Flask, g
from flask.ext.babel import Babel, lazy_gettext
from flask.ext import login
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand, Migrate


def gvars(app):
    @app.before_request
    def gdebug():
        if app.debug:
            g.debug = True
        else:
            g.debug = False

    @app.before_request
    def guser():
        g.user = login.current_user

    @app.context_processor
    def inject_user():
        try:
            return {'user': g.user}
        except AttributeError:
            return {'user': None}


def error_pages(app):
    # HTTP error pages definitions

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("misc/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("misc/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return render_template("misc/405.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("misc/500.html"), 500

        # @app.errorhandler(Exception)
        # def defaultHandler(e):
        # return 'ERROR! %s' % e, 500


def create_app(config=None, app_name='library'):
    app = Flask(app_name,
                static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
                template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates')
                )

    app.config.from_object('config')
    app.config.from_pyfile('../local.cfg', silent=True)
    if config:
        app.config.from_pyfile(config)

    error_pages(app)
    gvars(app)
    return app


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


