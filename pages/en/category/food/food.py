from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.en.category.food.introduction.introduction import food_introduction
from pages.en.category.food.basic.basic import food_basic
from pages.en.category.food.intermediary.intermediary import food_intermediary
from pages.en.category.food.advanced.advanced import food_advanced

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

food = Blueprint('food', __name__)

@food.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.en, lang_grid=SubCategory.en_option02, lang_meta=meta)

food.register_blueprint(food_introduction, url_prefix='/introduction')
food.register_blueprint(food_basic, url_prefix='/basic')
food.register_blueprint(food_intermediary, url_prefix='/intermediary')
food.register_blueprint(food_advanced, url_prefix='/advanced')