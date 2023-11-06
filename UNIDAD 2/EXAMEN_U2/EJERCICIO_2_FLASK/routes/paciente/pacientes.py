from flask import Blueprint,request,redirect,render_template,url_for
from models import Paciente
from forms import PacienteForm
from app import db

apppaciente = Blueprint('apppaciente',__name__,template_folder="templates")

@apppaciente.route('/')
@apppaciente.route('/index')

def inicio():
    pacientes = Paciente.query.all()
    return render_template('index.html', pacientes=pacientes)

@apppaciente.route('/agregar',methods=["GET","POST"])
def agregar():
    paciente = Paciente()
    pacienteForm = PacienteForm(obj=paciente)
    if request.method == 'POST':
        if pacienteForm.validate_on_submit():
            pacienteForm.populate_obj(paciente)
            db.session.add(paciente)
            db.session.commit()
            return redirect(url_for('apppaciente.inicio'))
    return render_template('agregar.html',forma=pacienteForm)

@apppaciente.route("/editar/<int:id>",methods=["GET", "POST"])
def editar(id):
    paciente = Paciente.query.get_or_404(id)
    pacienteForm = PacienteForm(obj=paciente)
    if(request.method == "POST"):
        if( pacienteForm.validate_on_submit() ):
            pacienteForm.populate_obj(paciente)
            db.session.commit()
            return redirect(url_for('apppaciente.inicio'))
    return render_template('editar.html',forma = pacienteForm)

@apppaciente.route('/eliminar/<int:id>')
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('apppaciente.inicio'))


