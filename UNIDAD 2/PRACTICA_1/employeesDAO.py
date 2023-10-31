from employees import Employee
from conecction import Conecction
from cursor_of_the_pool import Cursor_of_the_pool
from logger_base import log
import datetime

class EmployeeDAO:
    _SELECT = "SELECT * From employees WHERE status=true ORDER BY id" 
    _INSERT = "INSERT INTO employees(employeenumber, firstname, lastname, position, status, create_at, update_at) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    _UPDATE = "UPDATE employees SET employeenumber=%s, firstname=%s, lastname=%s, position=%s, status=%s, update_at=%s WHERE id=%s"
    _DELETE = "UPDATE employees SET status=%s WHERE id=%s" # Eliminación logica
    # _DELETE = "DELETE FROM employees WHERE id=%s"
    
    @classmethod
    def getAll(cls):
        with Cursor_of_the_pool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            employees = []
            for r in registros:
                employees.append(Employee(r[1], r[2], r[7], r[3], r[4]))
            return employees
    
    @classmethod
    def post(cls,employee:Employee):
        with Cursor_of_the_pool() as cursor:
            values = (employee.employeenumber, employee.firstname, employee.lastname, employee.position, employee.status, employee.create_at, employee.update_at)
            cursor.execute(cls._INSERT,values)
            return cursor.rowcount
    
    @classmethod
    def put(cls,employee:Employee):
        employee.update_at = datetime.datetime.now()
        with Cursor_of_the_pool() as cursor:
            values = (employee.employeenumber, employee.firstname, employee.lastname, employee.position, employee.status, employee.update_at, employee.id)
            cursor.execute(cls._UPDATE,values)
            return cursor.rowcount
        
    @classmethod
    def delete(cls,id_employee:int):
        with Cursor_of_the_pool() as cursor:
            value = (False, id_employee)
            cursor.execute(cls._DELETE,value)
            return cursor.rowcount
            
if __name__== "__main__":
    # # Insertar a la BD
    myEmployee = Employee(3434, "Pedro", "Perez", "Ingeniero", True, datetime.datetime.now(), datetime.datetime.now())
    insert = EmployeeDAO.post(myEmployee)
    log.debug(f"Empleado agregado: {insert}")
    # # Update
    myEmployee2 = Employee(112, "Juan", "Perez", "Cajero", True)
    myEmployee2.id = 1
    update = EmployeeDAO.put(myEmployee2)
    log.debug("Empleado actualizado")
    # # Delete
    delete = EmployeeDAO.delete(3)
    log.debug("Empleado eliminado")
    # Select de los registros en la BD
    employees = EmployeeDAO.getAll()
    for employee in employees:
        log.debug(employee)
        