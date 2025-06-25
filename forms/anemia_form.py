from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class AnemiaForm(FlaskForm):
    Gender = SelectField('Gender', choices=[('0', 'Female'), ('1', 'Male')], validators=[DataRequired()])
    Hemoglobin = FloatField('Hemoglobin', validators=[DataRequired(), NumberRange(min=7, max=16)])
    MCH = FloatField('MCH', validators=[DataRequired(), NumberRange(min=19, max=32)])
    MCHC = FloatField('MCHC', validators=[DataRequired(), NumberRange(min=29, max=36)])
    MCV = FloatField('MCV', validators=[DataRequired(), NumberRange(min=70, max=106)])
    submit = SubmitField('Submit')
