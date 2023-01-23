from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.pt.categoria.treinamento.introducao.introducao import treinamento_introducao
from pages.pt.categoria.treinamento.basico.basico import treinamento_basico
from pages.pt.categoria.treinamento.intermediario.intermediario import treinamento_intermediario
from pages.pt.categoria.treinamento.avancado.avancado import treinamento_avancado

meta = {
    'description': 'Tudo sobre treinamento de cães.',
    'keywords': 'treinamento de cão, treinamento de cães, treinamentos de cão, treinamentos de cães',
    'title': 'Tudo sobre treinamento de cães.',
}

treinamento = Blueprint('treinamento', __name__)

@treinamento.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.pt, lang_grid=SubCategory.pt_option04, lang_meta=meta)

treinamento.register_blueprint(treinamento_introducao, url_prefix='/introducao')
treinamento.register_blueprint(treinamento_basico, url_prefix='/basico')
treinamento.register_blueprint(treinamento_intermediario, url_prefix='/intermediario')
treinamento.register_blueprint(treinamento_avancado, url_prefix='/avancado')