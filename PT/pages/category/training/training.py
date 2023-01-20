from flask import Blueprint, render_template
from pages.category.training.advanced.advanced import training_advanced
from pages.category.training.basic.basic import training_basic
from pages.category.training.intermediary.intermediary import training_intermediary
from pages.category.training.intro.intro import training_intro

training = Blueprint('training', __name__)

@training.route("/")
def index():
    return render_template("category/training/training.html")

training.register_blueprint(training_advanced, url_prefix='/advanced')
training.register_blueprint(training_basic, url_prefix='/basic')
training.register_blueprint(training_intermediary, url_prefix='/intermediary')
training.register_blueprint(training_intro, url_prefix='/intro')