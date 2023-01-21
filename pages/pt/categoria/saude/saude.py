from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.pt.categoria.saude.introducao.introducao import saude_introducao
from pages.pt.categoria.saude.basico.basico import saude_basico
from pages.pt.categoria.saude.intermediario.intermediario import saude_intermediario
from pages.pt.categoria.saude.avancado.avancado import saude_avancado

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

saude = Blueprint('saude', __name__)

@saude.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.pt, lang_grid=SubCategory.pt_option03, lang_meta=meta)

saude.register_blueprint(saude_introducao, url_prefix='/introducao')
saude.register_blueprint(saude_basico, url_prefix='/basico')
saude.register_blueprint(saude_intermediario, url_prefix='/intermediario')
saude.register_blueprint(saude_avancado, url_prefix='/avancado')