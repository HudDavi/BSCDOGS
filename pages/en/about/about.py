from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

about = Blueprint('about', __name__)

@about.route("/")
def index():
    return render_template("about/about.html", lang_default=Default.en, lang_meta=meta)