from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

entrenamiento_avanzado = Blueprint('entrenamiento_avanzado', __name__)

@entrenamiento_avanzado.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@entrenamiento_avanzado.route("/01")
def post():
    return render_template("post/es/entrenamiento/avanzado/01.html", lang_default=Default.es, lang_meta=meta)