from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'Dog Food - Introduction.',
    'keywords': 'dog food, dogs food, dog foods, dogs foods',
    'title': 'Dog Food - Introduction.',
}

posts = {
    'posts_h1': '',
    'posts_href01': '',
    'posts_title01': '',
}

food_introduction = Blueprint('food_introduction', __name__)

@food_introduction.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta, lang_posts=posts)

@food_introduction.route("/01")
def post():
    return render_template("post/en/food/introduction/01.html", lang_default=Default.en, lang_meta=meta)