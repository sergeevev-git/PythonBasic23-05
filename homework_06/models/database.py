__all__ = ("Base", "db")

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
	def __tablename__(cls) -> str:
		return f"{cls.__name__.lower()}s"
	
	id = Column(Integer, primary_key = True)


db = SQLAlchemy(model_class = Base)
