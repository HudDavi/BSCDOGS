from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Saúde de Cães - Introdução.',
    'keywords': 'saúde de cães, saúde de um cão, saúde dos cães',
    'title': 'Saúde de Cães - Introdução.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

saude_introducao = Blueprint('saude_introducao', __name__)

@saude_introducao.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@saude_introducao.route("/01")
def post():
    return render_template("post/pt/saude/introducao/01.html", lang_default=Default.pt, lang_meta=meta)