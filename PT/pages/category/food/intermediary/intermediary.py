from flask import Blueprint, render_template

food_intermediary = Blueprint('food_intermediary', __name__)

@food_intermediary.route("/")
def index():
    return render_template("/category/food/intermediary/intermediary.html")

@food_intermediary.route("/01")
def post():
    return render_template("post/food/intermediary/01.html")