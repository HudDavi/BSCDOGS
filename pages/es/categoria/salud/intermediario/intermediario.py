from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Salud de Perros - Intermediario.',
    'keywords': 'salud de perros, salud de un perro, salud de los perros',
    'title': 'Salud de Perros - Intermediario.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

salud_intermediario = Blueprint('salud_intermediario', __name__)

@salud_intermediario.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@salud_intermediario.route("/01")
def post():
    return render_template("post/es/salud/intermediario/01.html", lang_default=Default.es, lang_meta=meta)