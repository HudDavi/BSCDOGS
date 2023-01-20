from flask import Blueprint, render_template

care_intermediary = Blueprint('care_intermediary', __name__)

@care_intermediary.route("/")
def index():
    return render_template("/category/care/intermediary/intermediary.html")

@care_intermediary.route("/01")
def post():
    return render_template("post/care/intermediary/01.html")