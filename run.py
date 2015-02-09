#!flask/bin/python
from library import manager, app

app.run(Debug=False)
manager.run()

