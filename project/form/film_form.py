
from flask_wtf import FlaskForm
from wtforms import (validators, StringField, IntegerField, TextAreaField, DateField, SubmitField)

from project.models.film import Film

class FilmForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired("Please enter the title."), validators.Length(min=2, max=70)])
    year = IntegerField('Year', [validators.DataRequired("Year is required"), validators.NumberRange(min=1895, max=2100)])
    description = TextAreaField('Description', [validators.DataRequired("Please enter the description"), validators.Length(min=1, max=500)])
    release_date = DateField('Release Date', [validators.DataRequired("Please enter the release date.")])
    duration = IntegerField('Duration', [validators.DataRequired("Duration is required"), validators.NumberRange(min=1, max=600)])
    btn_return = SubmitField(label='Return to list', render_kw={'formnovalidate': True})
    btn_cancel = SubmitField(label='Cancel', render_kw={'formnovalidate': True})
    btn_submit = SubmitField(label='Submit')

    def __init__(self, film_id=None, *args, **kwargs):  # accept the object
        super().__init__(*args, **kwargs)
        self.film_id = film_id

    """ unique title """
    def validate_title(self, field):
        search = True;
        if self.film_id != None:
            filmRecord = Film.query.get(self.film_id)
            if filmRecord.title == field.data.lower():
                search = False

        if search and Film.query.filter_by(title=field.data.lower()).first():
            raise validators.ValidationError('The title is already in use.')
