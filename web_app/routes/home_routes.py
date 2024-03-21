
from flask import Blueprint, render_template, current_app #, session

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return render_template("about.html")
