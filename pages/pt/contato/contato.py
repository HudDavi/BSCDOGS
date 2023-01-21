from flask import Blueprint, render_template
from pages.language.language import Default

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

contato = Blueprint('contato', __name__)

@contato.route("/")
def index():
    return render_template("contact/contact.html", lang_default=Default.pt, lang_meta=meta)