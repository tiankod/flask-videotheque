# routes
from flask import Blueprint, render_template
from project.models.film import Film

film_app = Blueprint('film_func', __name__)

@film_app.get('/')
def list() -> str:
    films = Film.query.all()
    return render_template('film/list.html', films=films)
