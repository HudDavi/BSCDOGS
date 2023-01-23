from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Alimentação de Cães - Intermediário.',
    'keywords': 'alimentação de cães, alimentação de um cão, alimentação dos cães',
    'title': 'Alimentação de Cães - Intermediário.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

alimentacao_intermediario = Blueprint('alimentacao_intermediario', __name__)

@alimentacao_intermediario.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@alimentacao_intermediario.route("/01")
def post():
    return render_template("post/pt/alimentacao/intermediario/01.html", lang_default=Default.pt, lang_meta=meta)