from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

treinamento_intermediario = Blueprint('treinamento_intermediario', __name__)

@treinamento_intermediario.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@treinamento_intermediario.route("/01")
def post():
    return render_template("post/pt/treinamento/intermediario/01.html", lang_default=Default.pt, lang_meta=meta)