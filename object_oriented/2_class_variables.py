# References https://www.youtube.com/watch?v=BJ-VvGyQxho
# Class variables shared among all instances of a class
# Instance variables can be unique

class Employee:
    num_of_emps = 0  # Tracker used to count number instances
    raise_amount = 1.04  # Class variable

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


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print("\n ------ \n")
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)  # Prints namespace of emp_1, no class variable
print(Employee.__dict__) # Prints namesspace of emp_1
print("\n ------ \n")
Employee.raise_amount = 1.05  # Affects all instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n ------ \n")
print(emp_1.__dict__)
emp_1.raise_amount = 1.06  # Only affects the one instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# raise_amount has been added as an instance variable for emp_1
print(emp_1.__dict__)
print(Employee.num_of_emps)