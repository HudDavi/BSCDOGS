from flask import Blueprint, render_template

food_advanced = Blueprint('food_advanced', __name__)

@food_advanced.route("/")
def index():
    return render_template("/category/food/advanced/advanced.html")

@food_advanced.route("/01")
def post():
    return render_template("post/food/advanced/01.html")