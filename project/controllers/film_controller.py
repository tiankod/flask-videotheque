# routes
from flask import Blueprint, render_template
from project.models.film import Film

film_app = Blueprint('film_func', __name__)

@film_app.get('/')
def list() -> str:
    films = Film.query.all()
    return render_template('film/list.html', films=films)

@film_app.get('/<int:film_id>/')
def display(film_id: int) -> str:
    film = Film.query.get_or_404(film_id)
    return render_template('film/detail.html', film=film)

