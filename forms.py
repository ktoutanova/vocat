from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddNumberForm(FlaskForm):
    title = StringField('Enter a Number Between 1 and 100', validators=[DataRequired()])
    submit = SubmitField('Submit')