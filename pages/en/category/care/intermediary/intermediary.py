from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Dog Care - Intermediary.',
    'keywords': 'dog care, dogs care, dog cares, dogs cares',
    'title': 'Dog Care - Intermediary.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

care_intermediary = Blueprint('care_intermediary', __name__)

@care_intermediary.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@care_intermediary.route("/01")
def post():
    return render_template("post/en/care/intermediary/01.html", lang_default=Default.en, lang_meta=meta)