from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Entrenamiento de Perros - Básico.',
    'keywords': 'entrenamiento de perros, entrenamiento de un perro, entrenamiento de los perros',
    'title': 'Entrenamiento de Perros - Básico.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

entrenamiento_basico = Blueprint('entrenamiento_basico', __name__)

@entrenamiento_basico.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@entrenamiento_basico.route("/01")
def post():
    return render_template("post/es/entrenamiento/basico/01.html", lang_default=Default.es, lang_meta=meta)