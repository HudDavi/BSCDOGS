from flask import Blueprint
from pages.es.comienzo.comienzo import comienzo
from pages.es.categoria.categoria import categoria
from pages.es.contacto.contacto import contacto
from pages.es.acerca.acerca import acerca

es = Blueprint('es', __name__, url_prefix='/')
es.register_blueprint(comienzo, url_prefix='/')
es.register_blueprint(categoria, url_prefix='/categoria')
es.register_blueprint(contacto, url_prefix='/contacto')
es.register_blueprint(acerca, url_prefix='/acerca')