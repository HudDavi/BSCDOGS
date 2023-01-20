from flask import Flask
from pages.about.about import about
from pages.contact.contact import contact
from pages.category.category import category
from pages.home.home import home

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(about, url_prefix='/about')
app.register_blueprint(category, url_prefix='/category')
app.register_blueprint(contact, url_prefix='/contact')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)