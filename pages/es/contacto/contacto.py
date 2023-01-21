from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

contacto = Blueprint('contacto', __name__)

@contacto.route("/")
def index():
    return render_template("contact/contact.html", lang_default=Default.es, lang_meta=meta)