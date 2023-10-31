from customers_suppliers import Customer_Supplier
from cursor_of_the_pool import Cursor_of_the_pool
from logger_base import log
import datetime

class CustomerDAO:
    _SELECT = "SELECT * From customers WHERE status=true ORDER BY id" 
    _INSERT = "INSERT INTO customers(name, adress, phonenumber, status, create_at, update_at) VALUES(%s,%s,%s,%s,%s,%s)"
    _UPDATE = "UPDATE customers SET name=%s, adress=%s, phonenumber=%s, status=%s, update_at=%s WHERE id=%s"
    _DELETE = "UPDATE customers SET status=%s WHERE id=%s" # Eliminación logica
    # _DELETE = "DELETE FROM employees WHERE id=%s"
    
    @classmethod
    def getAll(cls):
        with Cursor_of_the_pool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            customers = []
            for r in registros:
                customers.append(Customer_Supplier(r[1], r[2], r[3], r[4]))
            return customers
    
    @classmethod
    def post(cls,customer:Customer_Supplier):
        with Cursor_of_the_pool() as cursor:
            values = (customer.name, customer.adress, customer.phonenumber, customer.status, customer.create_at, customer.update_at)
            cursor.execute(cls._INSERT,values)
            return cursor.rowcount
    
    @classmethod
    def put(cls,customer:Customer_Supplier):
        customer.update_at = datetime.datetime.now()
        with Cursor_of_the_pool() as cursor:
            values = (customer.name, customer.adress, customer.phonenumber, customer.status, customer.update_at, customer.id)
            cursor.execute(cls._UPDATE,values)
            return cursor.rowcount
        
    @classmethod
    def delete(cls,id_customer:int):
        with Cursor_of_the_pool() as cursor:
            value = (False, id_customer)
            cursor.execute(cls._DELETE,value)
            return cursor.rowcount
            
if __name__== "__main__":
    # # Insertar a la BD
    myCustomer = Customer_Supplier("Pepsi", "Calle Priv. X", "1234567890", True, datetime.datetime.now(), datetime.datetime.now())
    insert = CustomerDAO.post(myCustomer)
    log.debug(f"Cliente agregado: {insert}")
    # # Update
    myEmployee2 = Customer_Supplier("Gamesa", "Calle Reforma", "1234567890", True)
    myEmployee2.id = 2
    update = CustomerDAO.put(myEmployee2)
    log.debug("Cliente actualizado")
    # # Delete
    delete = CustomerDAO.delete(4)
    log.debug("Empleado eliminado")
    # Select de los registros en la BD
    customers = CustomerDAO.getAll()
    for customer in customers:
        log.debug(customer)