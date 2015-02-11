# # -*- coding: utf-8 -*-
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

activate_this = os.path.join(PROJECT_DIR, 'venv', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

if not (PROJECT_DIR in sys.path):
    sys.path.append(PROJECT_DIR)

from library import app as application, create_app

app = create_app()
app.run(debug=False)

