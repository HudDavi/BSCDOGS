from flask import Blueprint, render_template

care_intro = Blueprint('care_intro', __name__)

@care_intro.route("/")
def index():
    return render_template("/category/care/intro/intro.html")

@care_intro.route("/01-a-amizade-entre-humanos-e-caes")
def post():
    return render_template("post/care/intro/01-a-amizade-entre-humanos-e-caes.html")
