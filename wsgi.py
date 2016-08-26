#! /usr/bin/env python

from wishlist import app, db
from wishlist.models import Message
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(Message(title="title", text="hello hi"))

    db.session.commit()
    print 'Initialized the database'

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
