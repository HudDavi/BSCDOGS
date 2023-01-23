from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.es.categoria.alimentacion.introduccion.introduccion import alimentacion_introduccion
from pages.es.categoria.alimentacion.basico.basico import alimentacion_basico
from pages.es.categoria.alimentacion.intermediario.intermediario import alimentacion_intermediario
from pages.es.categoria.alimentacion.avanzado.avanzado import alimentacion_avanzado

meta = {
    'description': 'Todo sobre alimentación de perros.',
    'keywords': 'alimentación de perro, alimentación de perros',
    'title': 'Todo sobre alimentación de perros.',
}

alimentacion = Blueprint('alimentacion', __name__)

@alimentacion.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.es, lang_grid=SubCategory.es_option02, lang_meta=meta)

alimentacion.register_blueprint(alimentacion_introduccion, url_prefix='/introduccion')
alimentacion.register_blueprint(alimentacion_basico, url_prefix='/basico')
alimentacion.register_blueprint(alimentacion_intermediario, url_prefix='/intermediario')
alimentacion.register_blueprint(alimentacion_avanzado, url_prefix='/avanzado')