from logger_base import log

class Animal:
    def __init__(self,id=None,raza=None,fechaingreso=None,fechasalida=None):
        self._id = id
        self._raza = raza
        self._fechaingreso = fechaingreso
        self._fechasalida = fechasalida

    def __str__(self) -> str:
        return f"""
        ID ANIMAL {self._id}
        RAZA {self._raza}
        FECHA DE INGRESO {self._fechaingreso}
        FECHA DE SALIDA {self._fechasalida}
        """
    
    @property
    def idAnimal(self):
        return self._id
    @idAnimal.setter
    def idAnimal(self,id):
        self.id= id

    @property
    def razaAnimal(self):
        return self._raza
    @razaAnimal.setter
    def razaAnimal(self,raza):
        self.raza = raza

    @property
    def ingresoAnimal(self):
        return self._fechaingreso
    @ingresoAnimal.setter
    def ingresoAnimal(self,fechaingreso):
        self.fechaingreso = fechaingreso

    @property
    def salidaAnimal(self):
        return self._fechasalida
    @salidaAnimal.setter
    def salidaAnimal(self,fechasalida):
        self.fechasalida = fechasalida

#if __name__=="__main__":
#    persona1 = Persona("cesar",8)
#    log.debug(persona1)
#    persona2 = Persona("alfonso",9)
#    log.debug(persona2)
#    persona3 = Persona("jordan",10)
#    log.debug(persona3)