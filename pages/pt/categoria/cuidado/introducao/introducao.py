from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

posts = {
    'posts_h1': 'Cuidado de Cães - Introdução',
    'posts_href01': '/pt/categoria/cuidado/introducao/01-a-amizade-entre-humanos-e-caes',
    'posts_title01': 'A amizade entre humanos e cães',
}

cuidado_introducao = Blueprint('cuidado_introducao', __name__)

@cuidado_introducao.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@cuidado_introducao.route("/01-a-amizade-entre-humanos-e-caes")
def post():
    return render_template("post/pt/cuidado/introducao/01.html", lang_default=Default.pt, lang_meta=meta)
