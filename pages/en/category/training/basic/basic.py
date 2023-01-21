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

training_basic = Blueprint('training_basic', __name__)

@training_basic.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@training_basic.route("/01")
def post():
    return render_template("post/en/training/basic/01.html", lang_default=Default.en, lang_meta=meta)