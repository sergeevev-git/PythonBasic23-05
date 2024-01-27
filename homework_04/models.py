"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, \
	async_sessionmaker

PG_CONN_URI = os.environ.get(
	"SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

async_engine = create_async_engine(
	url = PG_CONN_URI,
	echo = True,
)

async_session = async_sessionmaker(
	bind = async_engine,
	class_ = AsyncSession,
	expire_on_commit = False
	# получение данных с экземпляра без обновления из БД
)


# Base = DeclarativeBase()

class Base(DeclarativeBase):
	# @declared_attr.directive
	# def __tablename__(cls) -> str:
	# 	# prefix = config.TABLES_PREFIX
	# 	# return f"{prefix}{cls.__name__.lower()}s"
	# 	return f"{cls.__name__.lower()}s"
	
	id = Column(Integer, primary_key = True)


class User(Base):
	name = Column(String(100), nullable = False, unique = False)
	username = Column(String(32), nullable = False, unique = True)
	email = Column(String(120), nullable = True, unique = True)
	posts = relationship(
		'Post',
		# link to field
		back_populates = 'user',
		uselist = True  # one to many
	)


class Post(Base):
	title = Column(
		String(100),
		nullable = False,
		server_default = "",
		default = ""
	)
	body = Column(Text, nullable = False, unique = True)
	user_id = Column(String(120), nullable = True, unique = True)
	user = relationship(
		"User",
		back_populates = 'posts',
		uselist = False  # one to many
	)
