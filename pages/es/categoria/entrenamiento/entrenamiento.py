from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import SubCategory
from pages.es.categoria.entrenamiento.introduccion.introduccion import entrenamiento_introduccion
from pages.es.categoria.entrenamiento.basico.basico import entrenamiento_basico
from pages.es.categoria.entrenamiento.intermediario.intermediario import entrenamiento_intermediario
from pages.es.categoria.entrenamiento.avanzado.avanzado import entrenamiento_avanzado

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

entrenamiento = Blueprint('entrenamiento', __name__)

@entrenamiento.route("/")
def index():
    return render_template("category/subcategory/subcategory.html", lang_default=Default.es, lang_grid=SubCategory.es_option04, lang_meta=meta)

entrenamiento.register_blueprint(entrenamiento_introduccion, url_prefix='/introduccion')
entrenamiento.register_blueprint(entrenamiento_basico, url_prefix='/basico')
entrenamiento.register_blueprint(entrenamiento_intermediario, url_prefix='/intermediario')
entrenamiento.register_blueprint(entrenamiento_avanzado, url_prefix='/avanzado')