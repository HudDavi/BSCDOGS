from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.pt.categoria.alimentacao.introducao.introducao import alimentacao_introducao
from pages.pt.categoria.alimentacao.basico.basico import alimentacao_basico
from pages.pt.categoria.alimentacao.intermediario.intermediario import alimentacao_intermediario
from pages.pt.categoria.alimentacao.avancado.avancado import alimentacao_avancado

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

alimentacao = Blueprint('alimentacao', __name__)

@alimentacao.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.pt, lang_grid=SubCategory.pt_option02, lang_meta=meta)

alimentacao.register_blueprint(alimentacao_introducao, url_prefix='/introducao')
alimentacao.register_blueprint(alimentacao_basico, url_prefix='/basico')
alimentacao.register_blueprint(alimentacao_intermediario, url_prefix='/intermediario')
alimentacao.register_blueprint(alimentacao_avancado, url_prefix='/avancado')