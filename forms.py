from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddNumberForm(FlaskForm):
    title = StringField('Enter any Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RandomPageForm(FlaskForm):
    title = StringField('Go To Random Page')
    submit = SubmitField('Submit')