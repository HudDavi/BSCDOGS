from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.en.category.training.introduction.introduction import training_introduction
from pages.en.category.training.basic.basic import training_basic
from pages.en.category.training.intermediary.intermediary import training_intermediary
from pages.en.category.training.advanced.advanced import training_advanced

meta = {
    'description': 'All about training for dogs.',
    'keywords': 'training for dog, training for dogs, trainings for dog, trainings for dogs',
    'title': 'All about training for dogs.',
}

training = Blueprint('training', __name__)

@training.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.en, lang_grid=SubCategory.en_option04, lang_meta=meta)

training.register_blueprint(training_introduction, url_prefix='/introduction')
training.register_blueprint(training_basic, url_prefix='/basic')
training.register_blueprint(training_intermediary, url_prefix='/intermediary')
training.register_blueprint(training_advanced, url_prefix='/advanced')