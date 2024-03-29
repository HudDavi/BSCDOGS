from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Alimentación de Perros - Introducción.',
    'keywords': 'alimentación de perros, alimentación de un perro, alimentación de los perros',
    'title': 'Alimentación de Perros - Introducción.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

alimentacion_introduccion = Blueprint('alimentacion_introduccion', __name__)

@alimentacion_introduccion.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@alimentacion_introduccion.route("/01")
def post():
    return render_template("post/es/alimentacion/introduccion/01.html", lang_default=Default.es, lang_meta=meta)