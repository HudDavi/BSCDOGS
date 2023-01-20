from flask import Blueprint, render_template

training_basic = Blueprint('training_basic', __name__)

@training_basic.route("/")
def index():
    return render_template("/category/training/basic/basic.html")

@training_basic.route("/01")
def post():
    return render_template("post/training/basic/01.html")