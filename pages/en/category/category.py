from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category
from pages.en.category.care.care import care
from pages.en.category.food.food import food
from pages.en.category.health.health import health
from pages.en.category.training.training import training

meta = {
    'description': 'All about feeding, caring, health, and training dogs.',
    'keywords': 'feeding for dogs, caring for dogs, health for dogs, training for dogs',
    'title': 'All about feeding, caring, health, and training dogs.',
}

category = Blueprint('category', __name__)

@category.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.en, lang_grid=Category.en, lang_meta=meta)

category.register_blueprint(care, url_prefix='/care')
category.register_blueprint(food, url_prefix='/food')
category.register_blueprint(health, url_prefix='/health')
category.register_blueprint(training, url_prefix='/training')