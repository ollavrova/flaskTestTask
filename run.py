#!flask/bin/python
from library import manager, app

app.config(Debug=False)
manager.run()

