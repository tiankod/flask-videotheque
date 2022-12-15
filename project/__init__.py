from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

# configuration
app = Flask(__name__)
app.config.from_pyfile('config.py')

# bootstrap 5
bootstrap = Bootstrap5(app)

# En mode DEBUG uniquement, affichage de l'URI de la base de données
if app.config['DEBUG']:
    print("Database : " + app.config['SQLALCHEMY_DATABASE_URI'])

# config sqlalchemy
db = SQLAlchemy(app)

# page d'accueil
@app.get('/')
def home():
    return render_template('index.html')

# routes pour film
from .controllers import film_controller
app.register_blueprint(film_controller.film_app, url_prefix='/film')
