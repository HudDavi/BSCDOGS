from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Cuidado de Cães - Intermediário.',
    'keywords': 'cuidado de cães, cuidados de cães, cuidado de um cão, cuidados de um cão, cuidado dos cães, cuidados dos cães',
    'title': 'Cuidado de Cães - Intermediário.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

cuidado_intermediario = Blueprint('cuidado_intermediario', __name__)

@cuidado_intermediario.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@cuidado_intermediario.route("/01")
def post():
    return render_template("post/pt/cuidado/intermediario/01.html", lang_default=Default.pt, lang_meta=meta)