from flask import Blueprint
from pages.en.home.home import home
from pages.en.category.category import category
from pages.en.contact.contact import contact
from pages.en.about.about import about

en = Blueprint('en', __name__, url_prefix='/')
en.register_blueprint(home, url_prefix='/')
en.register_blueprint(category, url_prefix='/category')
en.register_blueprint(contact, url_prefix='/contact')
en.register_blueprint(about, url_prefix='/about')