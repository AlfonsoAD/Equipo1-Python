from logger_base import log
import datetime

class Employee:
    def __init__(self, employe_number = None, firstname = None, lastname = None, position = None, status = None, createat = None, updateat = None) -> None:
        self._employeenumber = employe_number
        self._firstname = firstname
        self._lastname = lastname
        self._position = position
        self._status = status
        self._create_at = createat
        self._update_at = updateat
    
    def __str__(self) -> str:
        return f"""
    No. Empleado:{self._employeenumber} Nombre: {self._firstname}
    Apellido:{self._lastname} Puesto:{self._position} Estatus:{self._status}
    """
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id_employee):
        self._id = id_employee
        
    @property
    def employeenumber(self):
        return self._employeenumber
    @employeenumber.setter  
    def employeenumber(self,employeenumber):
        self._employeenumber = employeenumber
        
    @property
    def firstname(self):
        return self._firstname
    @firstname.setter
    def firstname(self,firstname):
        self._firstname = firstname
        
    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self,lastname):
        self._lastname = lastname
        
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,position):
        self._position = position
        
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,status):
        self._status = status
        
    @property
    def create_at(self):
        return self._create_at
    @create_at.setter
    def create_at(self,create_at):
        self._create_at = create_at
        
    @property
    def update_at(self):
        return self._update_at
    @update_at.setter
    def update_at(self,update_at):
        self._update_at = update_at
        
if __name__ == "__main__":
    employee = Employee(1231,"Juan","Perez","Contador",True, datetime.datetime.now(), datetime.datetime.now())
    log.debug(employee)