from dotenv import load_dotenv
import os
from psycopg2 import pool
from logger_base import log

load_dotenv()

class Conecction:
    _DATABASE = os.getenv("DATABASE")
    _USERNAME = os.getenv("USERNAME")
    _PASSWORD = os.getenv("PASSWORD")
    _HOST = os.getenv("HOST")
    _PORT = os.getenv("PORT")
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def obtain_pool(cls):
        try:
            if cls._pool == None:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._PORT,
                    database = cls._DATABASE
                )
                log.debug(f"CREATION OF THE POOL {pool}")
                return cls._pool
            else:
                return cls._pool
        except Exception as e :
            log.error(e)
                
    @classmethod
    def obtain_connection(cls):
        connection = cls.obtain_pool().getconn()
        log.debug(f"CONNECTION OBTAINED {connection}")
        return connection
        
    @classmethod
    def release_connection(cls, conexion):
        cls.obtain_pool().putconn(conexion)
        log.debug(f"CONECCTION RETURNED {conexion}")
        
    @classmethod
    def close_connections(cls):
        cls.obtain_pool().closeall()
        log.debug("CONECCTIONS CLOSED")