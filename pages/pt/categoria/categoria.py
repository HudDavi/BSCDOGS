from flask import Blueprint, render_template
from pages.language.language import Default
from pages.language.language import Category
from pages.pt.categoria.cuidado.cuidado import cuidado
from pages.pt.categoria.alimentacao.alimentacao import alimentacao
from pages.pt.categoria.saude.saude import saude
from pages.pt.categoria.treinamento.treinamento import treinamento

meta = {
    'description': '',
    'keywords': '',
    'title': '',
}

categoria = Blueprint('categoria', __name__)

@categoria.route("/")
def index():
    return render_template("category/category.html", lang_default=Default.pt, lang_grid=Category.pt, lang_meta=meta)

categoria.register_blueprint(cuidado, url_prefix='/cuidado')
categoria.register_blueprint(alimentacao, url_prefix='/alimentacao')
categoria.register_blueprint(saude, url_prefix='/saude')
categoria.register_blueprint(treinamento, url_prefix='/treinamento')