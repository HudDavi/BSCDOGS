from flask import Blueprint, render_template
from pages.category.care.care import care
from pages.category.food.food import food
from pages.category.health.health import health
from pages.category.training.training import training

category = Blueprint('category', __name__)

@category.route("/")
def index():
    return render_template("category/category.html")

category.register_blueprint(care, url_prefix='/care')
category.register_blueprint(food, url_prefix='/food')
category.register_blueprint(health, url_prefix='/health')
category.register_blueprint(training, url_prefix='/training')