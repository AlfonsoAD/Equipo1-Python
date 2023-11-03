from flask import Blueprint,request,redirect,render_template,url_for
from models import Libro
from forms import LibrosForm
from app import db
from routes.editorial.editoriales import obtenerNombresEditoriales
from routes.autor.autores import obtenerNombresAutores

applibro = Blueprint('applibro',__name__,template_folder="templates")

@applibro.route('/')
@applibro.route('/index')
def inicio():
    libros = Libro.query.all()
    return render_template('index.html',libros=libros)

@applibro.route('/agregar',methods=["GET","POST"])
def agregar():
    libro=Libro()
    libroForm=LibrosForm(obj=libro)

    response = obtenerNombresEditoriales()
    if response.status_code == 200:
        nombres_editoriales = response.json['nombres_editoriales']
        libroForm.editorial.choices = [(nombre, nombre) for nombre in nombres_editoriales]

    response = obtenerNombresAutores()
    if response.status_code == 200:
        nombres_autores = response.json['nombres_autores']
        libroForm.autor.choices = [(nombre, nombre) for nombre in nombres_autores]

    if request.method == 'POST':
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            db.session.add(libro)
            db.session.commit()
            return redirect(url_for('applibro.inicio'))
    return render_template('agregar.html',formaLibros =libroForm)

@applibro.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    libro=Libro().query.get_or_404(id)
    libroForm = LibrosForm(obj=libro)

    response = obtenerNombresEditoriales()
    if response.status_code == 200:
        nombres_editoriales = response.json['nombres_editoriales']
        libroForm.editorial.choices = [(nombre, nombre) for nombre in nombres_editoriales]

    response = obtenerNombresAutores()
    if response.status_code == 200:
        nombres_autores = response.json['nombres_autores']
        libroForm.autor.choices = [(nombre, nombre) for nombre in nombres_autores]

    if request.method == "POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            db.session.commit()
            return redirect(url_for('applibro.inicio'))
    return render_template('editar.html',formaLibros=libroForm)

@applibro.route('/eliminar/<int:id>')
def eliminar(id):
    libro=Libro().query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('applibro.inicio'))