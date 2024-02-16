from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from views.users.views import users_app
from models import db

app = Flask(__name__)
app.register_blueprint(users_app)

# app.config.from_envvar()
# app.config.from_file()
CONFIG_NAME = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")
# app.config.update(
# 	SECRET_KEY = "secret",
# 	SQLALCHEMY_DATABASE_URI = config.DB_URL)

# import tomllib
# app.config.from_file("config.toml", load=tomllib.load, text=False)
# Or from a JSON file:
# import json
# app.config.from_file("config.json", load=json.load)


db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", endpoint = "index")
def root():
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug = True)
