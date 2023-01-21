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

health_basic = Blueprint('health_basic', __name__)

@health_basic.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@health_basic.route("/01")
def post():
    return render_template("post/en/health/basic/01.html", lang_default=Default.en, lang_meta=meta)