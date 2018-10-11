# References https://www.youtube.com/watch?v=rq8cL2XMM5M
# Regular methods in a class default take instance as first argument
# Class methods in a class default take class as first argument
# Static methods take neither as first argument, and don't operate on
# instance or on class

class Employee:
    num_of_emps = 0  # Tracker used to count number instances
    raise_amt = 1.04  # Class variable

    # self refers to the instance of the class
    def __init__(self, first, last, pay):  # Creates an instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # Need to access class variable via instance/class
        # Could also use Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # Decorator for defining a class method
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # Alternative constructor via class method
    # 'from' is common convention for naming - from_array, etc.
    # See datetime.py (common library) for examples
    def from_string(cls, emp_str):
        # Data is in string form
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # Decorator for defining static method
    # Doesn't access instance or class anywhere in function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
Employee.set_raise_amt(1.05)  # Same as Employee.raise_amt = 1.05
print("Raise amount set via class method")
print(Employee.raise_amt)  # Could be run on an instance too
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n------ String parsing below\n")
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email, new_emp_1.pay)  # From manual parsing
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email, new_emp_2.pay)  # From alternative constructor
print("\n------ Static methods below\n")
import datetime
my_date = datetime.date(2016, 7, 9)
print(Employee.is_workday(my_date))

