from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Dog Food - Intermediary.',
    'keywords': 'dog food, dogs food, dog foods, dogs foods',
    'title': 'Dog Food - Intermediary.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

food_intermediary = Blueprint('food_intermediary', __name__)

@food_intermediary.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@food_intermediary.route("/01")
def post():
    return render_template("post/en/food/intermediary/01.html", lang_default=Default.en, lang_meta=meta)