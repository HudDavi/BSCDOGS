from flask import Blueprint, render_template
from pages.language.language import Default

meta00 = {
    'description': 'Cuidado de Perros - Introducción.',
    'keywords': 'cuidado de perros, cuidados de perros, cuidado de un perro, cuidados de un perro, cuidado de los perros, cuidados de los perros',
    'title': 'Cuidado de Perros - Introducción.',
}

meta01 = {
    'description': 'Todo sobre la amistad entre humanos y perros.',
    'keywords': 'Todo sobre la amistad entre humanos y perros',
    'title': 'Todo sobre la amistad entre humanos y perros.',
}

posts = {
    'posts_h1': 'Cuidado de Perros - Introducción.',
    'posts_href01': '/es/categoria/cuidado/introduccion/todo-sobre-la-amistad-entre-humanos-y-perros',
    'posts_title01': 'Todo sobre la amistad entre humanos y perros.',
}

cuidado_introduccion = Blueprint('cuidado_introduccion', __name__)

@cuidado_introduccion.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta00, lang_posts=posts)

@cuidado_introduccion.route("/todo-sobre-la-amistad-entre-humanos-y-perros")
def post():
    return render_template("post/es/cuidado/introduccion/01.html", lang_default=Default.es, lang_meta=meta01)
