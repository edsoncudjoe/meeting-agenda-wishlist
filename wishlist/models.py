from datetime import datetime

from sqlalchemy import desc

from wishlist import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    @staticmethod
    def newest(num):
        return Message.query.order_by(desc(Message.id)).limit(num)
