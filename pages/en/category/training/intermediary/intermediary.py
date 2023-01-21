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

training_intermediary = Blueprint('training_intermediary', __name__)

@training_intermediary.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@training_intermediary.route("/01")
def post():
    return render_template("post/en/training/intermediary/01.html", lang_default=Default.en, lang_meta=meta)