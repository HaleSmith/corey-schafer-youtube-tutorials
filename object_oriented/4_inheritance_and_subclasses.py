# References https://www.youtube.com/watch?v=RSl87lqOXDE
# Inheritance allows attributes and methods to be inherited from a
# parent class
# Can use parent class as a template and override features without
# altering original


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # Inherits all functionality of parent
    # Doesn't change attribute of parent class
    raise_amt = 1.10  # Overrides that of parent class

    # Alternate constructor with additional attribute
    def __init__(self, first, last, pay, prog_lang):
        # Initializes the parent class
        super().__init__(first, last, pay)
        # Could have also typed:
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    # Don't pass mutable data types (list, dict) as default argument
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



# During initialization, found no __init__ method, so looked up the
# chain of inheritance to initialize. Chain is called the "method
# resolution order"
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.email)
print(dev_2.email)
print(help(Developer))  # Mentions method resolution order
print("\nApply raise below\n")
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print("\nTest prog_lang attribute below")
print(dev_1.email)
print(dev_1.prog_lang)
print("\nTest manager class below")
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
print("After added emp_2")
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
print("After remove emp_1")
mgr_1.print_emps()
print("\nisinstance issubclass below\n")
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

# Additional examples in exceptions.py of Whiskey library