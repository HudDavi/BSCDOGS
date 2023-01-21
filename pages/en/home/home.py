from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

home = Blueprint('home', __name__, url_prefix='/')

@home.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.en, lang_grid=Category.en, lang_meta=meta)