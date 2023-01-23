from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Alimentación de Perros - Básico.',
    'keywords': 'alimentación de perros, alimentación de un perro, alimentación de los perros',
    'title': 'Alimentación de Perros - Básico.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

alimentacion_basico = Blueprint('alimentacion_basico', __name__)

@alimentacion_basico.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@alimentacion_basico.route("/01")
def post():
    return render_template("post/es/alimentacion/basico/01.html", lang_default=Default.es, lang_meta=meta)