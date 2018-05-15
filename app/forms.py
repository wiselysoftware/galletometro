from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Nombre Obligatorio"), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(message="Correo Obligatorio"),
                                             Length(max=24),
                                             Email(message="Correo invalido")])
    message = TextAreaField('Algun mensaje?', validators=[Length(max=400)])
    submit = SubmitField('Enviar')
