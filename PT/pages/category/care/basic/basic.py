from flask import Blueprint, render_template

care_basic = Blueprint('care_basic', __name__)

@care_basic.route("/")
def index():
    return render_template("/category/care/basic/basic.html")

@care_basic.route("/01")
def post():
    return render_template("post/care/basic/01.html")