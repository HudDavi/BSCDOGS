from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Entrenamiento de Perros - Introducción.',
    'keywords': 'entrenamiento de perros, entrenamiento de un perro, entrenamiento de los perros',
    'title': 'Entrenamiento de Perros - Introducción.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

entrenamiento_introduccion = Blueprint('entrenamiento_introduccion', __name__)

@entrenamiento_introduccion.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@entrenamiento_introduccion.route("/01")
def post():
    return render_template("post/es/entrenamiento/introduccion/01.html", lang_default=Default.es, lang_meta=meta)