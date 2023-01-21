from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

comienzo = Blueprint('comienzo', __name__, url_prefix='/')

@comienzo.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.es, lang_grid=Category.es, lang_meta=meta)