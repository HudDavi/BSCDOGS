from flask import Blueprint, render_template

health_advanced = Blueprint('health_advanced', __name__)

@health_advanced.route("/")
def index():
    return render_template("/category/health/advanced/advanced.html")

@health_advanced.route("/01")
def post():
    return render_template("post/health/advanced/01.html")