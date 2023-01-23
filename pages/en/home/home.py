from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category

meta = {
    'description': 'All about feeding, caring, health, and training dogs.',
    'keywords': 'feeding for dogs, caring for dogs, health for dogs, training for dogs',
    'title': 'All about feeding, caring, health, and training dogs.',
}

home = Blueprint('home', __name__, url_prefix='/')

@home.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.en, lang_grid=Category.en, lang_meta=meta)