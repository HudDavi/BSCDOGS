from flask import Flask
from pages.pages import pages
from pages.en.en import en
from pages.es.es import es
from pages.pt.pt import pt

app = Flask(__name__)
app.register_blueprint(pages, url_prefix='/')
app.register_blueprint(en, url_prefix='/en')
app.register_blueprint(es, url_prefix='/es')
app.register_blueprint(pt, url_prefix='/pt')

if __name__ == "__main__":
    app.run(host='52.41.36.82', port=8000)