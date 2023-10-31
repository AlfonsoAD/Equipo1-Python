from logger_base import log
import datetime

class Customer_Supplier:
    def __init__(self, name = None, adress = None, phonenumber = None, status = None, createat = None, updateat = None) -> None:
        self._name = name
        self._adress = adress
        self._phonenumber = phonenumber
        self._status = status
        self._create_at = createat
        self._update_at = updateat
    
    def __str__(self) -> str:
        return f"""
    Nombre:{self._name} Dirección: {self._adress}
    No. Telefono:{self._phonenumber} Estatus:{self._status}
    """
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id_customer):
        self._id = id_customer
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
        
    @property
    def adress(self):
        return self._adress
    @adress.setter
    def lastname(self,address):
        self._adress = address
        
    @property
    def phonenumber(self):
        return self._phonenumber
    @phonenumber.setter
    def phonenumber(self,phone):
        self._phonenumber = phone
        
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
    customer = Customer_Supplier("Cliente", "Calle 1", "1234567890", True, datetime.datetime.now(), datetime.datetime.now())
    log.debug(customer)