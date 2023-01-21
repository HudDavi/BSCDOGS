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

cuidado_introduccion = Blueprint('cuidado_introduccion', __name__)

@cuidado_introduccion.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@cuidado_introduccion.route("/01-a-amizade-entre-humanos-e-caes")
def post():
    return render_template("post/es/cuidado/introduccion/01-a-amizade-entre-humanos-e-caes.html", lang_default=Default.es, lang_meta=meta)
