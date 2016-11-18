from app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    album = db.relationship("Photo")

    __tablename__ = 'users'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s/%s" % (self.username, self.password)

class Photo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    tn_url = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')
    tags = db.relationship('Tag', cascade='all, delete, delete-orphan')

    __tablename__ = 'photos'

class Tag(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'))
    attr = db.Column(db.String(20))

    photo = db.relationship('Photo')

    __tablename__ = "tags"
