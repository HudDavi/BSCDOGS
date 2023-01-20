from flask import Blueprint, render_template

food_basic = Blueprint('food_basic', __name__)

@food_basic.route("/")
def index():
    return render_template("/category/food/basic/basic.html")

@food_basic.route("/01")
def post():
    return render_template("post/food/basic/01.html")