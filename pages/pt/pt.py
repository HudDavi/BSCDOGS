from flask import Blueprint
from pages.pt.inicio.inicio import inicio
from pages.pt.categoria.categoria import categoria

pt = Blueprint('pt', __name__, url_prefix='/')
pt.register_blueprint(inicio, url_prefix='/')
pt.register_blueprint(categoria, url_prefix='/categoria')