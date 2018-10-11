# References https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# Classes allow functions and data to be grouped
# Attributes are data associated with a class
# Methods are functions associated with a class
# Class is blue print for an instance


class Employee:
    pass  # This allows a class to be defined as a stub


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)  # Prints memory address
print(emp_1)  # Prints memory address

emp_1.first = 'Corey'
emp_2.first = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.first = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)  # Extra fields can be added to a class
print(emp_2.email)  # Email field not in class definition

print("Deleting values")
del emp_1, emp_2, Employee


class Employee:
    # self refers to the instance of the class
    def __init__(self, first, last, pay):  # Creates an instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Corey', 'Schafer', 50000)  # Runs __init__
emp_2 = Employee('Test', 'User', 60000)  # Don't need to pass self

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname)  # Prints the memory location of method
print(emp_2.fullname)  # Prints the memory location of method
print(emp_1.fullname())
print(emp_2.fullname())

# This is what print(emp_1.fullname()) is doing
print(Employee.fullname(emp_1))  # Can run class method on an instance
