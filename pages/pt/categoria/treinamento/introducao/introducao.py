from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Treinamento de Cães - Introdução.',
    'keywords': 'treinamento de cães, treinamento de um cão, treinamento dos cães',
    'title': 'Treinamento de Cães - Introdução.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

treinamento_introducao = Blueprint('treinamento_introducao', __name__)

@treinamento_introducao.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@treinamento_introducao.route("/01")
def post():
    return render_template("post/pt/treinamento/introducao/01.html", lang_default=Default.pt, lang_meta=meta)