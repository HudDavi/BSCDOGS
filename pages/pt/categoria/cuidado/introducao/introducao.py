from flask import Blueprint, render_template
from pages.language.language import Default

meta00 = {
    'description': 'Cuidado de Cães - Introdução.',
    'keywords': 'cuidado de cães, cuidados de cães, cuidado de um cão, cuidados de um cão, cuidado dos cães, cuidados dos cães',
    'title': 'Cuidado de Cães - Introdução.',
}

meta01 = {
    'description': 'Tudo sobre a amizade entre humanos e cães.',
    'keywords': 'Tudo sobre a amizade entre humanos e cães',
    'title': 'Tudo sobre a amizade entre humanos e cães.',
}

posts = {
    'posts_h1': 'Cuidado de Cães - Introdução.',
    'posts_href01': '/pt/categoria/cuidado/introducao/tudo-sobre-a-amizade-entre-humanos-e-caes',
    'posts_title01': 'Tudo sobre a amizade entre humanos e cães.',
}

cuidado_introducao = Blueprint('cuidado_introducao', __name__)

@cuidado_introducao.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta00, lang_posts=posts)

@cuidado_introducao.route("/tudo-sobre-a-amizade-entre-humanos-e-caes")
def post():
    return render_template("post/pt/cuidado/introducao/01.html", lang_default=Default.pt, lang_meta=meta01)
