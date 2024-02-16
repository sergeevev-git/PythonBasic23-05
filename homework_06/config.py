from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
	"SQLALCHEMY_DATABASE_URI",
	"postgresql+psycopg://user:example@localhost:5432/postgres"
)


class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = "secret"
	SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
	SECRET_KEY = ("...",)  # read from secret_file


class DevelopmentConfig(Config):
	DEBUG = True
	TESTING = False


class TestingConfig(Config):
	DEBUG = True
	TESTING = True
