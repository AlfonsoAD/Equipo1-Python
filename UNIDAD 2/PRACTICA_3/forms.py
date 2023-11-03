from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

generos = ['Terror', 'Drama', 'Romance']

class LibrosForm(FlaskForm):
    titulo = StringField('Titulo',validators=[DataRequired()])
    autor = SelectField('Autor')
    editorial = SelectField('Editorial')
    year = IntegerField('Año de publicacion')
    genero = SelectField("Selecciona un Genero", choices=generos)
    enviar = SubmitField("Enviar")

class EditorialForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    pais = StringField('Pais')
    telefono = IntegerField('Numero Telefonico')
    enviar = SubmitField("Enviar")
