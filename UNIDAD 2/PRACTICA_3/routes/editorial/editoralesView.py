from flask import Blueprint,request,redirect,render_template,url_for
from models import Editorial
from forms import EditorialForm
from app import db

appeditorialesv = Blueprint('appeditorialesv',__name__,template_folder="templates")

@appeditorialesv.route('/')
@appeditorialesv.route('/editoriales')
def inicioEditorial():
    editoriales = Editorial.query.all()
    return render_template('indexEditorial.html',editoriales=editoriales)

@appeditorialesv.route('/agregarEditoriales',methods=["GET","POST"])
def agregarEditoriales():
    editorial=Editorial()
    editorialForm=EditorialForm(obj=editorial)

    if request.method == 'POST':
        if editorialForm.validate_on_submit():
            editorialForm.populate_obj(editorial)
            db.session.add(editorial)
            db.session.commit()
            return redirect(url_for('appeditorialesv.inicioEditorial'))
    return render_template('agregarEditoriales.html',editorialForma =editorialForm)

@appeditorialesv.route('/editarEditoriales/<int:id>',methods=['GET','POST'])
def editarEditoriales(id):
    editorial=Editorial().query.get_or_404(id)
    editorialForm = EditorialForm(obj=editorial)
    if request.method == "POST":
        if editorialForm.validate_on_submit():
            editorialForm.populate_obj(editorial)
            db.session.commit()
            return redirect(url_for('appeditorialesv.inicioEditorial'))
    return render_template('editarEditoriales.html',editorialForma=editorialForm)

@appeditorialesv.route('/eliminarEditoriales/<int:id>')
def eliminarEditoriales(id):
    editorial=Editorial().query.get_or_404(id)
    db.session.delete(editorial)
    db.session.commit()
    return redirect(url_for('appeditorialesv.inicioEditorial'))