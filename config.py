# -*- coding: utf-8 -*-

# DEBUG = True
DEBUG = False
from os.path import dirname, abspath

# SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/data.sqlite' % dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'postgres://dzqkyovdaypqxz:X0B7trV4gruKRC4OxCdbvYNH-x@ec2-174-129-213-103.compute-1.amazonaws.com:5432/de793kf29b1fmv'

CSRF_ENABLED = True
SECRET_KEY = 'fghfgjlkl12356f8gdf8fgfh78j9h8h7drferew'