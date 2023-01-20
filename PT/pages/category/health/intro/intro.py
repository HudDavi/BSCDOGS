from flask import Blueprint, render_template

health_intro = Blueprint('health_intro', __name__)

@health_intro.route("/")
def index():
    return render_template("/category/health/intro/intro.html")

@health_intro.route("/01")
def post():
    return render_template("post/health/intro/01.html")