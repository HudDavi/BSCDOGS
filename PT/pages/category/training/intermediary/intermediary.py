from flask import Blueprint, render_template

training_intermediary = Blueprint('training_intermediary', __name__)

@training_intermediary.route("/")
def index():
    return render_template("/category/training/intermediary/intermediary.html")

@training_intermediary.route("/01")
def post():
    return render_template("post/training/intermediary/01.html")