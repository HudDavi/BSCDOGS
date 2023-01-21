from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

pages = Blueprint('pages', __name__, url_prefix='/')

@pages.route("/")
def index():
    return render_template("index/index.html", lang_default=Default.en, lang_meta=meta)