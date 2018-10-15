# Does script off of file, see sqlite_demo_ram for script off of ram
# Need to keep deleting .db file when running this script

# References https://www.youtube.com/watch?v=pd-0G0MigUA
# Link contains more links to other SQL tutorials
# Connecting makes file if it exists, oterhwise just connects
# Docstring quotes when multiple commands
# sqlite data type documentation at https://www.sqlite.org/datatype3.html
# Making table from memory each time is for fast development
# Use syntax at bottom of file to prevent injection attack


import sqlite3
from employee import Employee

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Create a new application with employee info")
print("Create a new database connection. See employee.db")

# Can make an in memory database or on disk
# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('employee.db')  # Makes dbase if not exist
print("Make a cursor so commands can be accessed")
c = conn.cursor()
# First/last name data type is text, pay is integer data type
print("Make a table and define fields")
try:
    c.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")
    print("Commit the current transaction")
    conn.commit()
except Exception as e:
    print(f"Exception: {e}")
conn.close()

new_section("Add in data")
conn = sqlite3.connect('employee.db')
c = conn.cursor()
print("Use sqlite3 INSERT command for class attributes")
c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")
conn.commit()
conn.close()

new_section("Query data")
conn = sqlite3.connect('employee.db')
c = conn.cursor()
print("Accesing data via SELECT query")
c.execute("SELECT * FROM employees WHERE first='Mary'")
print("Fetching next value from cursor")
# Could also do fetchmany(5) to fetch that # of rows, or fetchall
print(c.fetchall())
conn.commit()
conn.close()

new_section("Add in data via a Python class")
conn = sqlite3.connect('employee.db')
c = conn.cursor()
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
# Below is vulnerable to SQL injection attacks
# c.execute(f"INSERT INTO employees VALUES ('{emp_1.first}', "
#           f"'{emp_1.last}', {emp_1.pay})")
# c.execute(f"INSERT INTO employees VALUES ('{emp_2.first}', "
#           f"'{emp_2.last}', {emp_2.pay})")
print("Injection attack prevention method 1")
c.execute("INSERT INTO employees VALUES (?, ?, ?)",
          (emp_1.first, emp_1.last, emp_1.pay))
print("Injection attack prevention method 2 (Cody's favorite)")
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
          {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
conn.commit()
conn.close()

new_section("Query data via ?")
conn = sqlite3.connect('employee.db')
c = conn.cursor()
print("Get all entries with last name Schafer via simple ? method")
# Need comma at end to make argument a tuple
c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
print(c.fetchall())
print("Get all entries with last name Doe via clean dict method")
c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
print(c.fetchall())