from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Saúde de Cães - Avançado.',
    'keywords': 'saúde de cães, saúde de um cão, saúde dos cães',
    'title': 'Saúde de Cães - Avançado.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

saude_avancado = Blueprint('saude_avancado', __name__)

@saude_avancado.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@saude_avancado.route("/01")
def post():
    return render_template("post/pt/saude/avancado/01.html", lang_default=Default.pt, lang_meta=meta)