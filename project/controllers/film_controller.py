''' 
    routes pour l'entité Film
'''
from flask import Blueprint, render_template, Response, redirect, url_for, request
from project.form.film_form import FilmForm
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

@film_app.route('/create/', methods=('GET', 'POST'))
def create() -> str | Response :
    form = FilmForm()

    if request.method == 'POST':
        if form.btn_return.data:
            return redirect(url_for('film_func.list'))

        if form.btn_cancel.data:
            return redirect(url_for('film_func.create'))
            
        if form.validate():
            film = Film(form.title.data, form.year.data, form.description.data, form.release_date.data, form.duration.data)
            db.session.add(film)
            db.session.commit()
            return redirect(url_for('film_func.list'))

    title = 'Add a New Film'
    return render_template('film/form.html', title=title, form = form)

@film_app.route('/<int:film_id>/form/', methods=('GET', 'POST'))
def edit(film_id: int) -> str | Response:

    form = FilmForm(film_id=film_id)

    if request.method == 'POST': 
        if form.btn_return.data:
            return redirect(url_for('film_func.list'))

        if form.btn_cancel.data:
            film: Film = Film.query.get_or_404(film_id)
            return redirect(url_for('film_func.edit', film_id=film.id))

        if form.validate():
            filmRecord: Film = Film.query.get_or_404(film_id)
            filmView = Film(form.title.data, form.year.data, form.description.data, form.release_date.data, form.duration.data)
            filmRecord.title = filmView.title
            filmRecord.year = filmView.year
            filmRecord.description = filmView.description
            filmRecord.release_date = filmView.release_date
            filmRecord.duration = filmView.duration
            db.session.add(filmRecord)
            db.session.commit()
            return redirect(url_for('film_func.list'))

    film: Film = Film.query.get_or_404(film_id)
    title = f'{film.title} {film.year} \'s Details ' 
    form.title.data = film.title
    form.year.data = film.year
    form.description.data = film.description
    form.release_date.data = film.release_date
    form.duration.data = film.duration
    return render_template('film/form.html', title=title, form=form)
