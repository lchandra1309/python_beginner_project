from employee_class import Employee
import empdatabase

emp1=Employee('lokesh',25,'annotator')
emp2=Employee('malini',28,'validator')
emp3=Employee('praba',26,'validator')
emp4=Employee('venkat',32,'teamlead',8)
emp5=Employee('rajan',35,'manager',10)

empdatabase.insert_into(emp1)
empdatabase.insert_into(emp2)
empdatabase.insert_into(emp3)
empdatabase.insert_into(emp4)
empdatabase.insert_into(emp5)

empdatabase.delete_database()