from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.pt.categoria.cuidado.introducao.introducao import cuidado_introducao
from pages.pt.categoria.cuidado.basico.basico import cuidado_basico
from pages.pt.categoria.cuidado.intermediario.intermediario import cuidado_intermediario
from pages.pt.categoria.cuidado.avancado.avancado import cuidado_avancado

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

cuidado = Blueprint('cuidado', __name__)

@cuidado.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.pt, lang_grid=SubCategory.pt_option01, lang_meta=meta)

cuidado.register_blueprint(cuidado_introducao, url_prefix='/introducao')
cuidado.register_blueprint(cuidado_basico, url_prefix='/basico')
cuidado.register_blueprint(cuidado_intermediario, url_prefix='/intermediario')
cuidado.register_blueprint(cuidado_avancado, url_prefix='/avancado')