from flask import Blueprint, render_template
from pages.language.language import Default

meta00 = {
    'description': 'Dog Care - Introduction.',
    'keywords': 'dog care, dogs care, dog cares, dogs cares',
    'title': 'Dog Care - Introduction.',
}

meta01 = {
    'description': 'All about the friendship between humans and dogs.',
    'keywords': 'All about the friendship between humans and dogs',
    'title': 'All about the friendship between humans and dogs.',
}

posts = {
    'posts_h1': 'Dog Care - Introduction.',
    'posts_href01': '/en/category/care/introduction/all-about-the-friendship-between-humans-and-dogs',
    'posts_title01': 'All about the friendship between humans and dogs.',
}

care_introduction = Blueprint('care_introduction', __name__)

@care_introduction.route("/")
def index():
    return render_template("/category/subcategory/posts/posts.html", lang_default=Default.en, lang_meta=meta00, lang_posts=posts)

@care_introduction.route("/all-about-the-friendship-between-humans-and-dogs")
def post():
    return render_template("post/en/care/introduction/01.html", lang_default=Default.en, lang_meta=meta01)
