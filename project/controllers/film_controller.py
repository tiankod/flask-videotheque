''' 
    routes pour l'entité Film
'''
from flask import Blueprint, render_template, Response, redirect, url_for
from project.models.film import Film
from project import db

film_app = Blueprint('film_func', __name__)

@film_app.get('/')
def list() -> str:
    films = Film.query.all()
    return render_template('film/list.html', films=films)

@film_app.get('/<int:film_id>/')
def display(film_id: int) -> str:
    film = Film.query.get_or_404(film_id)
    return render_template('film/detail.html', film=film)

@film_app.post('/<int:film_id>/delete/')
def delete(film_id: int) -> Response:
    film = Film.query.get_or_404(film_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('film_func.list'))
