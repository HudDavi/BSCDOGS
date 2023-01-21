from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.en.category.care.introduction.introduction import care_introduction
from pages.en.category.care.basic.basic import care_basic
from pages.en.category.care.intermediary.intermediary import care_intermediary
from pages.en.category.care.advanced.advanced import care_advanced

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

care = Blueprint('care', __name__)

@care.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.en, lang_grid=SubCategory.en_option01, lang_meta=meta)

care.register_blueprint(care_introduction, url_prefix='/introduction')
care.register_blueprint(care_basic, url_prefix='/basic')
care.register_blueprint(care_intermediary, url_prefix='/intermediary')
care.register_blueprint(care_advanced, url_prefix='/advanced')