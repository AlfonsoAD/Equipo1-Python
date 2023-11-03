from flask import Blueprint,jsonify,request
from models import Autor
from app import db

appautor = Blueprint("appautor",__name__)

@appautor.route('/autor/agregar',methods=['POST'])
def agregarAutor():
    try:
        json = request.get_json()
        autor=Autor()
        autor.nombre=json['nombre']
        autor.nacionalidad=json['nacionalidad']
        db.session.add(autor)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Autor"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@appautor.route('/autor/editar',methods=['POST'])
def editarAutor():
    try:
        json = request.get_json()
        autor=Autor.query.get_or_404(json["id"])
        autor.nombre=json['nombre']
        autor.nacionalidad =json['nacionalidad']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Autor modificado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@appautor.route('/autor/eliminar',methods=['POST'])
def eliminarAutor():
    try:
        json = request.get_json()
        autor=Autor.query.get_or_404(json["id"])
        db.session.delete(autor)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Autor eliminado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@appautor.route('/autor/nombres', methods=['GET'])
def obtenerNombresAutores():
    try:
        autores = Autor.query.all()
        nombres_autores = [autor.nombre for autor in autores]
        return jsonify({"status": 200, "nombres_autores": nombres_autores})
    except Exception as ex:
        return jsonify({"status": 400, "mensaje":ex})