from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Cuidado de Perros - Avanzado.',
    'keywords': 'cuidado de perros, cuidados de perros, cuidado de un perro, cuidados de un perro, cuidado de los perros, cuidados de los perros',
    'title': 'Cuidado de Perros - Avanzado.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

cuidado_avanzado = Blueprint('cuidado_avanzado', __name__)

@cuidado_avanzado.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@cuidado_avanzado.route("/01")
def post():
    return render_template("post/es/cuidado/avanzado/01.html", lang_default=Default.es, lang_meta=meta)