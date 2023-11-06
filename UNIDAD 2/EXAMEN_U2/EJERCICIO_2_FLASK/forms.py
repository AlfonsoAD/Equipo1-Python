from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class PacienteForm(FlaskForm):
    nombre = StringField('Alias o Nombre',validators=[DataRequired()])
    tipo = StringField('Tipo (perro,gato, etc)',validators=[DataRequired()])
    raza = StringField('Raza (Ej. Gran danes, etc)',validators=[DataRequired()])
    alergias = StringField('Alergias: Si o NO',validators=[DataRequired()])
    enviar = SubmitField('Guardar', render_kw={"class": "btn btn-success"})
