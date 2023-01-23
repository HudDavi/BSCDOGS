from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Dog Health - Advanced.',
    'keywords': 'dog health, dogs health',
    'title': 'Dog Health - Advanced.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

health_advanced = Blueprint('health_advanced', __name__)

@health_advanced.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@health_advanced.route("/01")
def post():
    return render_template("post/en/health/advanced/01.html", lang_default=Default.en, lang_meta=meta)