from flask import Blueprint, render_template

health_intermediary = Blueprint('health_intermediary', __name__)

@health_intermediary.route("/")
def index():
    return render_template("/category/health/intermediary/intermediary.html")

@health_intermediary.route("/01")
def post():
    return render_template("post/health/intermediary/01.html")