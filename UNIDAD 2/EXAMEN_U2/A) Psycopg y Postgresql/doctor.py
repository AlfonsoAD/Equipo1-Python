from logger_base import log

class Doctor:
    def __init__(self,id,nombre,numerotelefono):
        self._id = id
        self._nombre = nombre
        self._numerotelefono = numerotelefono
    
    def __str__(self) -> str:
        return f"""
        ID DOCTOR {self._id}
        NOMBRE {self._nombre}
        NUMERO DE TELEFONO {self._numerotelefono}
        """
    
    @property
    def idDoctor(self):
        return self._id
    @idDoctor.setter
    def idDoctor(self,id):
        self.id= id

    @property
    def nombreDoctor(self):
        return self._nombre
    @nombreDoctor.setter
    def nombreDoctor(self,nombre):
        self.nombre= nombre
    
    @property
    def telefonoDoctor(self):
        return self._numerotelefono
    @telefonoDoctor.setter
    def telefonoDoctor(self,numerotelefono):
        self.numerotelefono = numerotelefono