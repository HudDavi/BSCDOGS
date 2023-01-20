from flask import Blueprint, render_template

training_advanced = Blueprint('training_advanced', __name__)

@training_advanced.route("/")
def index():
    return render_template("/category/training/advanced/advanced.html")

@training_advanced.route("/01")
def post():
    return render_template("post/training/advanced/01.html")