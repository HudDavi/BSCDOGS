from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category
from pages.es.categoria.cuidado.cuidado import cuidado
from pages.es.categoria.alimentacion.alimentacion import alimentacion
from pages.es.categoria.salud.salud import salud
from pages.es.categoria.entrenamiento.entrenamiento import entrenamiento

meta = {
    'description': 'Todo sobre alimentación, cuidado, salud y entrenamiento de perros.',
    'keywords': 'alimentación de perros, cuidado de perros, salud de perros, entrenamiento de perros',
    'title': 'Todo sobre alimentación, cuidado, salud y entrenamiento de perros.',
}

categoria = Blueprint('categoria', __name__)

@categoria.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.es, lang_grid=Category.es, lang_meta=meta)

categoria.register_blueprint(cuidado, url_prefix='/cuidado')
categoria.register_blueprint(alimentacion, url_prefix='/alimentacion')
categoria.register_blueprint(salud, url_prefix='/salud')
categoria.register_blueprint(entrenamiento, url_prefix='/entrenamiento')