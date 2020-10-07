from employee_class import Employee
import sqlite3

def start():
   global db
   global cursor
   db=sqlite3.Connection('employee.db')
   cursor=db.cursor()
   cursor.execute("""CREATE TABLE IF NOT EXISTS employee(name TEXT,age INT,position TEXT,experience NULL)""")
   return cursor 
   

def insert_into(object):
    c=start()
    c.execute('INSERT INTO employee VALUES(?,?,?,?)',(object.name,object.age,object.position,object.exp))
    db.commit()
    db.close()
    print('successfully inserted with row id {}'.format(c.lastrowid))

def delete_database():
    c=start()
    c.execute('DROP TABLE employee')
    db.commit()
    db.close()
    print('sucessfully deleted all the contents in the table')