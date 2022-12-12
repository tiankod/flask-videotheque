from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_bootstrap import Bootstrap5

# configuration
app = Flask(__name__)
app.config.from_pyfile('config.py')

# page d'accueil
@app.get('/')
def home():
    return render_template('index.html')

# bootstrap 5
bootstrap = Bootstrap5(app)

"""
if app.config['DEBUG']:
    print("Database : " + app.config['SQLALCHEMY_DATABASE_URI'])

# config sqlalchemy
db = SQLAlchemy(app)


# page d'accueil
@app.get('/')
def home():
    return render_template('index.html')

# routes pour student
from .controllers import student_controller
app.register_blueprint(student_controller.student_app, url_prefix='/student')

"""