from customers_suppliers import Customer_Supplier
from cursor_of_the_pool import Cursor_of_the_pool
from logger_base import log
import datetime

class SupplierDAO:
    _SELECT = "SELECT * From suppliers WHERE status=true ORDER BY id" 
    _INSERT = "INSERT INTO suppliers(name, adress, phonenumber, status, create_at, update_at) VALUES(%s,%s,%s,%s,%s,%s)"
    _UPDATE = "UPDATE suppliers SET name=%s, adress=%s, phonenumber=%s, status=%s, update_at=%s WHERE id=%s"
    _DELETE = "UPDATE suppliers SET status=%s WHERE id=%s" # Eliminación logica
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
    def post(cls,supplier:Customer_Supplier):
        with Cursor_of_the_pool() as cursor:
            values = (supplier.name, supplier.adress, supplier.phonenumber, supplier.status, supplier.create_at, supplier.update_at)
            cursor.execute(cls._INSERT,values)
            return cursor.rowcount
    
    @classmethod
    def put(cls,supplier:Customer_Supplier):
        supplier.update_at = datetime.datetime.now()
        with Cursor_of_the_pool() as cursor:
            values = (supplier.name, supplier.adress, supplier.phonenumber, supplier.status, supplier.update_at, supplier.id)
            cursor.execute(cls._UPDATE,values)
            return cursor.rowcount
        
    @classmethod
    def delete(cls,id_supplier:int):
        with Cursor_of_the_pool() as cursor:
            value = (False, id_supplier)
            cursor.execute(cls._DELETE,value)
            return cursor.rowcount
            
if __name__== "__main__":
    # # Insertar a la BD
    mySupplier = Customer_Supplier("Bokados", "Calle Z", "1234567890", True, datetime.datetime.now(), datetime.datetime.now())
    insert = SupplierDAO.post(mySupplier)
    log.debug(f"Proveedor agregado: {insert}")
    # # Update
    mySupplier2 = Customer_Supplier("Marinela", "Calle Reforma Acueducto", "1234567890", True)
    mySupplier2.id = 3
    update = SupplierDAO.put(mySupplier2)
    log.debug("Proveedor actualizado")
    # # Delete
    delete = SupplierDAO.delete(4)
    log.debug("Proveedor eliminado")
    # Select de los registros en la BD
    customers = SupplierDAO.getAll()
    for customer in customers:
        log.debug(customer)