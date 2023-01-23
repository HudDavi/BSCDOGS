from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Dog Food - Basic.',
    'keywords': 'dog food, dogs food, dog foods, dogs foods',
    'title': 'Dog Food - Basic.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

food_basic = Blueprint('food_basic', __name__)

@food_basic.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@food_basic.route("/01")
def post():
    return render_template("post/en/food/basic/01.html", lang_default=Default.en, lang_meta=meta)