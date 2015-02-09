# -*- coding: utf-8 -*-

# DEBUG = True
DEBUG = False
from os.path import dirname, abspath

SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/data.sqlite' % dirname(abspath(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'fghfgjlkl12356f8gdf8fgfh78j9h8h7drferew'