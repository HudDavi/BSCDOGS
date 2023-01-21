from flask import Blueprint
from pages.pt.inicio.inicio import inicio
from pages.pt.categoria.categoria import categoria
from pages.pt.contato.contato import contato
from pages.pt.sobre.sobre import sobre

pt = Blueprint('pt', __name__, url_prefix='/')
pt.register_blueprint(inicio, url_prefix='/')
pt.register_blueprint(categoria, url_prefix='/categoria')
pt.register_blueprint(contato, url_prefix='/contato')
pt.register_blueprint(sobre, url_prefix='/sobre')