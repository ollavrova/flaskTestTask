# # -*- coding: utf-8 -*-
from library.app import manager

manager.add_option('-c', '--config', dest="config", required=False,
                   help="config file")

if __name__ == "__main__":
    manager.run()
