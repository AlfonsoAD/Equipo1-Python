from logger_base import log

class Consulta:
    def __init__(self,id,id_animal,id_doctor, servicio, cost):
        self._id = id
        self._idAnimal = id_animal
        self._idDoctor = id_doctor
        self._servicio = servicio
        self._cost = cost

    def __str__(self) -> str:
        return f"""
        ID CONSULTA {self._id}
        ID ANIMAL {self._idAnimal}
        ID DOCTOR {self._idDoctor}
        ID SERVICIO {self._servicio}
        ID COSTO {self._cost}
        """
    
    property
    def idConsulta(self):
        return self._id
    @idConsulta.setter
    def idConsulta(self,id):
        self.id= id

    property
    def idAnimal(self):
        return self._idAnimal
    @idAnimal.setter
    def idAnimal(self,id_animal):
        self.id_animal= id_animal
    
    property
    def idDoctor(self):
        return self._idDoctor
    @idDoctor.setter
    def idDoctor(self,id_doctor):
        self.id_doctor= id_doctor

    property
    def servicioCon(self):
        return self._servicio
    @servicioCon.setter
    def servicioCon(self,servicio):
        self.servicio= servicio

    property
    def costoCon(self):
        return self._cost
    @costoCon.setter
    def costoCon(self,costo):
        self.costo = costo
