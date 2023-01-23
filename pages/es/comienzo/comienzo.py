from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category

meta = {
    'description': 'Todo sobre alimentación, cuidado, salud y entrenamiento de perros.',
    'keywords': 'alimentación de perros, cuidado de perros, salud de perros, entrenamiento de perros',
    'title': 'Todo sobre alimentación, cuidado, salud y entrenamiento de perros.',
}

comienzo = Blueprint('comienzo', __name__, url_prefix='/')

@comienzo.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.es, lang_grid=Category.es, lang_meta=meta)