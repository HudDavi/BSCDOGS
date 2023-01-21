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

salud_basico = Blueprint('salud_basico', __name__)

@salud_basico.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.es, lang_meta=meta, lang_posts=posts)

@salud_basico.route("/01")
def post():
    return render_template("post/es/salud/basico/01.html", lang_default=Default.es, lang_meta=meta)