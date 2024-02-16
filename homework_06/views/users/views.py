from flask import Blueprint, flash, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest
from models import User
from . import crud

users_app = Blueprint("users_app", __name__, url_prefix = "/users")


@users_app.get("/", endpoint = "list")
def get_users_list():
	return render_template(
		"users/index.html",
		users = crud.get_user_list(),
	)


@users_app.get("/<int:user_id>/", endpoint = "details")
def get_users_by_name_or_raise(user_id: int):
	user: User = crud.get_user_by_id(user_id)
	
	return render_template(
		"users/details.html",
		user = user,
	)


@users_app.route("/create/", endpoint = "create", methods = ["GET", "POST"])
def create_new_user():
	if request.method == "GET":
		return render_template("users/create.html")
	
	user_name = request.form.get("user_name", "")
	user_name = user_name.strip()
	if not user_name:
		raise BadRequest("`user_name` field required")
	
	user_username = request.form.get("user_username", "")
	user_username = user_username.strip()
	if not user_username:
		raise BadRequest("`user_username` field required")
	
	user_email = request.form.get("user_email", "")
	user_email = user_email.strip()
	if not user_email:
		raise BadRequest("`user_email` field required")
	
	user = crud.create_user(name = user_name, username = user_username,
	                        email = user_email)
	
	flash(f"Created user {user.name}", category = "success")
	
	url = url_for("users_app.details", user_id = user.id)
	return redirect(url)


@users_app.route(
	"/<int:user_id>/confirm-delete/",
	endpoint = "delete",
	methods = ["GET", "POST"],
)
def delete_user(user_id: int):
	user = crud.get_user_by_id(user_id)
	if request.method == "GET":
		return render_template("users/confirm-delete.html",
		                       user = user)
	
	flash(f"Deleted user {user.name}", category = "warning")
	crud.delete_user(user)
	url = url_for("users_app.list")
	return redirect(url)
