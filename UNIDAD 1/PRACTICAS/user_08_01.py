#8 Resumen y multi-solución
# 8.1.-Definir una clase usuario que contenga como atributos: 
# Usuario
# Contraseña
# Rol
# Nombre
# CURP
# Ciudad

class user:
    @property    
    def user(self) -> str:
        return self.__user
    
    @property
    def password(self):
        return self.__password
    
    @property    
    def rol(self) -> str:
        return self.__rol
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property    
    def CURP(self) -> str:
        return self.__CURP
    
    @property
    def city(self) -> str:
        return self.__city
        
    @user.setter
    def __set_user(self,user:str) -> str:
        self.__user = user
    
    @password.setter
    def __set_password(self,password) -> str:
        self.__password = password
        
    @rol.setter
    def __set_rol(self,rol:str) -> str:
        self.__rol = rol
    
    @name.setter
    def __set_name(self,name:str) -> str:
        self.__name = name
    
    @CURP.setter
    def __set_curp(self,curp:str) -> str:
        self.__CURP = curp
    
    @city.setter
    def __set_city(self,city:str) -> str:
        self.__city = city
    
    def registrar(self, user:str, password:str, name:str, curp:str, city:str, rol:str = "Cliente"):
        self.__set_user = user
        self.__set_password = password
        self.__set_name = name
        self.__set_curp = curp
        self.__set_city = city
        self.__set_rol = rol
        
        