from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Dog Care - Basic.',
    'keywords': 'dog care, dogs care, dog cares, dogs cares',
    'title': 'Dog Care - Basic.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

care_basic = Blueprint('care_basic', __name__)

@care_basic.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@care_basic.route("/01")
def post():
    return render_template("post/en/care/basic/01.html", lang_default=Default.en, lang_meta=meta)