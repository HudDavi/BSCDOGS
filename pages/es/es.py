from flask import Blueprint
from pages.es.comienzo.comienzo import comienzo
from pages.es.categoria.categoria import categoria

es = Blueprint('es', __name__, url_prefix='/')
es.register_blueprint(comienzo, url_prefix='/')
es.register_blueprint(categoria, url_prefix='/categoria')