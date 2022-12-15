""" class Film """

from datetime import date
from sqlalchemy import func
from project import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(500), nullable=False)
    release_date = db.Column(db.DateTime(timezone=True))
    duration = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, title: str, year: int, description: str, release_date: date, duration: int):
        self.title = title
        self.year = year
        self.description = description
        self.release_date = release_date
        self.duration = duration

    def __repr__(self) -> str:
        return f'<Film {self.title} {self.year}>'
