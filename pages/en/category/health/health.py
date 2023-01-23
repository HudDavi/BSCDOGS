from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.en.category.health.introduction.introduction import health_introduction
from pages.en.category.health.basic.basic import health_basic
from pages.en.category.health.intermediary.intermediary import health_intermediary
from pages.en.category.health.advanced.advanced import health_advanced

meta = {
    'description': 'All about health for dogs.',
    'keywords': 'health for dog, health for dogs',
    'title': 'All about health for dogs.',
}

health = Blueprint('health', __name__)

@health.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.en, lang_grid=SubCategory.en_option03, lang_meta=meta)

health.register_blueprint(health_introduction, url_prefix='/introduction')
health.register_blueprint(health_basic, url_prefix='/basic')
health.register_blueprint(health_intermediary, url_prefix='/intermediary')
health.register_blueprint(health_advanced, url_prefix='/advanced')