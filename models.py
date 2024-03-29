"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)

class User(db.Model):
    """User"""
    __tablename__ = 'users'
    icon = '/static/user.png'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(40),
                           nullable=False)
    last_name = db.Column(db.String(40))
    image_url = db.Column(db.String,
                          nullable=False,
                          default=icon)
