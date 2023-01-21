from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

contact = Blueprint('contact', __name__)

@contact.route("/")
def index():
    return render_template("contact/contact.html", lang_default=Default.en, lang_meta=meta)