# # -*- coding: utf-8 -*-
import os
import sys

# PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = u'/home/krocozabr/mysite/flaskTestTask/'

if not (PROJECT_DIR in sys.path):
    sys.path.append(PROJECT_DIR)

from library import app as application, create_app





