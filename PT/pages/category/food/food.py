from flask import Blueprint, render_template
from pages.category.food.advanced.advanced import food_advanced
from pages.category.food.basic.basic import food_basic
from pages.category.food.intermediary.intermediary import food_intermediary
from pages.category.food.intro.intro import food_intro

food = Blueprint('food', __name__)

@food.route("/")
def index():
    return render_template("category/food/food.html")

food.register_blueprint(food_advanced, url_prefix='/advanced')
food.register_blueprint(food_basic, url_prefix='/basic')
food.register_blueprint(food_intermediary, url_prefix='/intermediary')
food.register_blueprint(food_intro, url_prefix='/intro')