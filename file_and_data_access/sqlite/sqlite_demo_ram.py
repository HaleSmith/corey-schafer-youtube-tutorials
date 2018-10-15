# Does script off of ram
# References https://www.youtube.com/watch?v=pd-0G0MigUA

import sqlite3
from employee import Employee

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Create a new application with employee info")
print("Create a new database connection in RAM")
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
conn.commit()

def insert_emp(emp):
    with conn: # Automatically handles closing the connection, etc.
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    # Not need context manager because is a read-only operation
    c.execute("SELECT * FROM employees WHERE last=:last",
              {'last': 'Doe'})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


new_section("Insert employees")
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
insert_emp(emp_1)
insert_emp(emp_2)

new_section("Get employees")
emps = get_emps_by_name('Doe')
print(emps)

new_section("Update employees and display")
update_pay(emp_2, 95000)
remove_emp(emp_1)
emps = get_emps_by_name('Doe')
print(emps)

conn.close()