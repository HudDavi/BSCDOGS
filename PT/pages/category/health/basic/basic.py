from flask import Blueprint, render_template

health_basic = Blueprint('health_basic', __name__)

@health_basic.route("/")
def index():
    return render_template("/category/health/basic/basic.html")

@health_basic.route("/01")
def post():
    return render_template("post/health/basic/01.html")