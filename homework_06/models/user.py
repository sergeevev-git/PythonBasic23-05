from sqlalchemy import Column, String
from .database import db


class User(db.Model):
	name = Column(String(100), nullable = False, unique = False)
	username = Column(String(32), nullable = False, unique = True)
	email = Column(String(120), nullable = True, unique = True)
# posts = db.relationship("Post", backref = 'user', lazy = 'dynamic')
