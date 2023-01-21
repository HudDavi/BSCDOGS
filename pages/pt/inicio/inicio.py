from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

inicio = Blueprint('inicio', __name__, url_prefix='/')

@inicio.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.pt, lang_grid=Category.pt, lang_meta=meta)