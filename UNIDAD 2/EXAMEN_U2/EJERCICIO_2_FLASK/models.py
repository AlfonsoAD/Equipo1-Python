from app import db

class Doctor(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    domicilio = db.Column(db.String(250))

class Cliente(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellido= db.Column(db.String(255))
    email = db.Column(db.String(255))
    domicilio = db.Column(db.String(250))
    
class Paciente(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
    raza = db.Column(db.String(255))
    alergias = db.Column(db.String(250))

class Accesorios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(255))
    precio = db.Column(db.Integer)
    descripcion = db.Column(db.String(250))
    stock = db.Column(db.String(250))

class Proveedores(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
    marca = db.Column(db.String(250))
    direccion = db.Column(db.String(250))




