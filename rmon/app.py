#!/usr/bin/env python3

import urllib
from rmon.app import create_app
from rmon.models import db

app = create_app()

@app.cli.command()
def init_db():
    pass
    print ("sqlite3 database file is %s" % app.config["SQLALCHEMY_DATABASE_URI"])
    db.create_all()
