from flask import Blueprint, render_template
from pages.category.health.advanced.advanced import health_advanced
from pages.category.health.basic.basic import health_basic
from pages.category.health.intermediary.intermediary import health_intermediary
from pages.category.health.intro.intro import health_intro

health = Blueprint('health', __name__)

@health.route("/")
def index():
    return render_template("category/health/health.html")

health.register_blueprint(health_advanced, url_prefix='/advanced')
health.register_blueprint(health_basic, url_prefix='/basic')
health.register_blueprint(health_intermediary, url_prefix='/intermediary')
health.register_blueprint(health_intro, url_prefix='/intro')