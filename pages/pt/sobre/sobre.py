from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

sobre = Blueprint('sobre', __name__)

@sobre.route("/")
def index():
    return render_template("about/about.html", lang_default=Default.pt, lang_meta=meta)