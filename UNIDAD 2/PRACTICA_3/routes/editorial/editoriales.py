from flask import Blueprint,jsonify,request
from models import Editorial
from app import db

appeditorial = Blueprint("appeditorial",__name__)

@appeditorial.route('/editorial/agregar',methods=['POST'])
def agregarEditorial():
    try:
        json = request.get_json()
        editorial=Editorial()
        editorial.nombre=json['nombre']
        editorial.pais=json['pais']
        editorial.telefono=json['telefono']
        db.session.add(editorial)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Editorial"})
    except Exception as ex:
        error_message = str(ex)  # Obtener el mensaje de error como una cadena
        return jsonify({"status": 400, "mensaje": error_message})
    
@appeditorial.route('/editorial/editar',methods=['POST'])
def editarEditorial():
    try:
        json = request.get_json()
        editorial=Editorial.query.get_or_404(json["id"])
        editorial.nombre=json['nombre']
        editorial.pais=json['pais']
        editorial.telefono=json['telefono']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Editorial modificado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@appeditorial.route('/editorial/eliminar',methods=['POST'])
def eliminarEditorial():
    try:
        json = request.get_json()
        editorial=Editorial.query.get_or_404(json["id"])
        db.session.delete(editorial)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Editorial eliminado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@appeditorial.route('/editorial/nombres', methods=['GET'])
def obtenerNombresEditoriales():
    try:
        editorales = Editorial.query.all()
        nombres_editoriales = [editorial.nombre for editorial in editorales]
        return jsonify({"status": 200, "nombres_editoriales": nombres_editoriales})
    except Exception as ex:
        return jsonify({"status": 400, "mensaje":ex})