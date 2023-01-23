from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Cuidado de Cães - Básico.',
    'keywords': 'cuidado de cães, cuidados de cães, cuidado de um cão, cuidados de um cão, cuidado dos cães, cuidados dos cães',
    'title': 'Cuidado de Cães - Básico.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

cuidado_basico = Blueprint('cuidado_basico', __name__)

@cuidado_basico.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@cuidado_basico.route("/01")
def post():
    return render_template("post/pt/cuidado/basico/01.html", lang_default=Default.pt, lang_meta=meta)