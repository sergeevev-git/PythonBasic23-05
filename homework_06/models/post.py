from sqlalchemy import Column, String, Text, Integer, ForeignKey
from .database import db


class Post(db.Model):
	title = Column(String(100), nullable = False, server_default = "",
	               default = "")
	body = Column(Text, nullable = False, unique = True)
	user_id = Column(Integer, ForeignKey('user.id'))
