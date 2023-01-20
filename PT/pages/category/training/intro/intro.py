from flask import Blueprint, render_template

training_intro = Blueprint('training_intro', __name__)

@training_intro.route("/")
def index():
    return render_template("/category/training/intro/intro.html")

@training_intro.route("/01")
def post():
    return render_template("post/training/intro/01.html")