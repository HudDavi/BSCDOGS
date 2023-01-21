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

health_intermediary = Blueprint('health_intermediary', __name__)

@health_intermediary.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@health_intermediary.route("/01")
def post():
    return render_template("post/en/health/intermediary/01.html", lang_default=Default.en, lang_meta=meta)