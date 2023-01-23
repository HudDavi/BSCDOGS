from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category

meta = {
    'description': 'Tudo sobre alimentação, cuidado, saúde, e treinamento de cães.',
    'keywords': 'alimentação de cães, cuidado de cães, saúde de cães, treinamento de cães',
    'title': 'Tudo sobre alimentação, cuidado, saúde, e treinamento de cães.',
}

inicio = Blueprint('inicio', __name__, url_prefix='/')

@inicio.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.pt, lang_grid=Category.pt, lang_meta=meta)