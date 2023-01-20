from flask import Blueprint, render_template

food_intro = Blueprint('food_intro', __name__)

@food_intro.route("/")
def index():
    return render_template("/category/food/intro/intro.html")

@food_intro.route("/01")
def post():
    return render_template("post/food/intro/01.html")