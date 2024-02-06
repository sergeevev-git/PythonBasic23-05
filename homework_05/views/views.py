from flask import Blueprint, render_template

about_app = Blueprint(
	"about_app",
	__name__,
	url_prefix = "/about"
)


@about_app.get("/", endpoint = "about")
def get_products_list():
	return render_template("about.html")
