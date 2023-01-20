from flask import Blueprint, render_template
from pages.category.care.advanced.advanced import care_advanced
from pages.category.care.basic.basic import care_basic
from pages.category.care.intermediary.intermediary import care_intermediary
from pages.category.care.intro.intro import care_intro

care = Blueprint('care', __name__)

@care.route("/")
def index():
    return render_template("category/care/care.html")

care.register_blueprint(care_advanced, url_prefix='/advanced')
care.register_blueprint(care_basic, url_prefix='/basic')
care.register_blueprint(care_intermediary, url_prefix='/intermediary')
care.register_blueprint(care_intro, url_prefix='/intro')