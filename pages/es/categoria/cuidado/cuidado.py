from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.es.categoria.cuidado.introduccion.introduccion import cuidado_introduccion
from pages.es.categoria.cuidado.basico.basico import cuidado_basico
from pages.es.categoria.cuidado.intermediario.intermediario import cuidado_intermediario
from pages.es.categoria.cuidado.avanzado.avanzado import cuidado_avanzado

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

cuidado = Blueprint('cuidado', __name__)

@cuidado.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.es, lang_grid=SubCategory.es_option01, lang_meta=meta)

cuidado.register_blueprint(cuidado_introduccion, url_prefix='/introduccion')
cuidado.register_blueprint(cuidado_basico, url_prefix='/basico')
cuidado.register_blueprint(cuidado_intermediario, url_prefix='/intermediario')
cuidado.register_blueprint(cuidado_avanzado, url_prefix='/avanzado')