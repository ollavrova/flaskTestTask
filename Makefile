all: setup
	. venv/bin/activate; python manage.py db init
	. venv/bin/activate; python manage.py db upgrade

venv/bin/activate:
	$(venv_run) venv

init: venv/bin/activate
	. venv/bin/activate; python manage.py db init


downgrade: venv/bin/activate
	. venv/bin/activate; python manage.py db downgrade

setup: venv/bin/activate requirements.txt
	. venv/bin/activate; pip install -r requirements.txt

run: venv/bin/activate requirements.txt
	. venv/bin/activate; python manage.py runserver -h 0.0.0.0 -d -r

migrate: venv/bin/activate
	. venv/bin/activate; python manage.py db upgrade

test: venv/bin/activate;
	. venv/bin/activate; python -m unittest tests




	
