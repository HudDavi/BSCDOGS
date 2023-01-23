from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.es.categoria.salud.introduccion.introduccion import salud_introduccion
from pages.es.categoria.salud.basico.basico import salud_basico
from pages.es.categoria.salud.intermediario.intermediario import salud_intermediario
from pages.es.categoria.salud.avanzado.avanzado import salud_avanzado

meta = {
    'description': 'Todo sobre salud de perros.',
    'keywords': 'salud de perro, salud de perros',
    'title': 'Todo sobre salud de perros.',
}

salud = Blueprint('salud', __name__)

@salud.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.es, lang_grid=SubCategory.es_option03, lang_meta=meta)

salud.register_blueprint(salud_introduccion, url_prefix='/introduccion')
salud.register_blueprint(salud_basico, url_prefix='/basico')
salud.register_blueprint(salud_intermediario, url_prefix='/intermediario')
salud.register_blueprint(salud_avanzado, url_prefix='/avanzado')