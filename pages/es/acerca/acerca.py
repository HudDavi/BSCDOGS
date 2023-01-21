from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

acerca = Blueprint('acerca', __name__)

@acerca.route("/")
def index():
    return render_template("about/about.html", lang_default=Default.es, lang_meta=meta)