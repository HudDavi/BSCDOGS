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

training_advanced = Blueprint('training_advanced', __name__)

@training_advanced.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@training_advanced.route("/01")
def post():
    return render_template("post/en/training/advanced/01.html", lang_default=Default.en, lang_meta=meta)