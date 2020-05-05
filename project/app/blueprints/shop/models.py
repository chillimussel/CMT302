"""
shop model definition
"""
from app import db
import datetime as dt

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),nullable=False)
    price = db.Column(db.Float,nullable=False)
    desc = db.Column(db.Text,nullable=False)
    image = db.Column(db.String(1024),nullable=False) # for storing image path
    inventory = db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return '<Item {}>'.format(self.name)

class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    item = db.relationship('Item', backref=db.backref('wishes'),lazy=True)
    user = db.relationship('User',backref=db.backref('wishes'),lazy=True)
    created = db.Column(db.DateTime, default=dt.datetime.now,nullable=False)
    def __repr__(self):
        return "<User {}>'s whish item created at {}".format(
            self.user.username,
            self.created.strftime('%Y-%X')
        )

