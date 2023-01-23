from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': 'All about feeding, caring, health, and training dogs.',
    'keywords': 'feeding for dogs, caring for dogs, health for dogs, training for dogs',
    'title': 'All about feeding, caring, health, and training dogs.',
}

pages = Blueprint('pages', __name__, url_prefix='/')

@pages.route("/")
def index():
    return render_template("index/index.html", lang_default=Default.en, lang_meta=meta)