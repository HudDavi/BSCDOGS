from flask import Blueprint
from pages.en.home.home import home
from pages.en.category.category import category

en = Blueprint('en', __name__, url_prefix='/')
en.register_blueprint(home, url_prefix='/')
en.register_blueprint(category, url_prefix='/category')