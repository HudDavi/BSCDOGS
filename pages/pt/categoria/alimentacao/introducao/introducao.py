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

alimentacao_introducao = Blueprint('alimentacao_introducao', __name__)

@alimentacao_introducao.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.pt, lang_meta=meta, lang_posts=posts)

@alimentacao_introducao.route("/01")
def post():
    return render_template("post/pt/alimentacao/introducao/01.html", lang_default=Default.pt, lang_meta=meta)