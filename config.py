# -*- coding: utf-8 -*-
import os
from os.path import dirname, abspath
DEBUG = True

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://krocozabr:348348@mysql.server/krocozabr$default'
# SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/data.sqlite' % dirname(abspath(__file__))


CSRF_ENABLED = True
SECRET_KEY = 'fghfgjlkl12356f8gdf8fgfh78j9h8h7drferew'



