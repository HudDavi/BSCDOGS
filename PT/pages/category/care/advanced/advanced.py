from flask import Blueprint, render_template

care_advanced = Blueprint('care_advanced', __name__)

@care_advanced.route("/")
def index():
    return render_template("/category/care/advanced/advanced.html")

@care_advanced.route("/01")
def post():
    return render_template("post/care/advanced/01.html")