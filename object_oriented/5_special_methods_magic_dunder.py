# References https://www.youtube.com/watch?v=3ohzBxoFHAY
# References https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
# See datetime.py in standard library for more overloading examples
# Special methods/magic methods allow mimicry of internal Python
# There should be a return NotImplemented to prevent errors
# functions and operator overloading
class Employee:

    raise_amt = 1.04

    # Dunder init means init surrounded by double underscores
    # Implicitly called when instance initialized
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Implicitly defined in a class
    # Meant to be unambiguous representation of object
    # Used for debugging, logging, seen by other developers
    # Need repr as minimum, because str will call it if str not exist
    # Return a string that can be used to reproduce the object
    # Should be as if could copy-paste to Python and make same object
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    # Implicitly defined in a class
    # Intended to be readable, as display to end user
    def __str__(self):
        return f"{self.fullname()}, {self.email}"

    # Overloading + operator to add salary of two employees
    def __add__(self, other):  # Other is another instance from class
        return self.pay + other.pay
        # if some condition isn't met, return NotImplemented

    # Overloading length operator to know full name length
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(type(emp_1.email))  # Verify that f-string is still string
print(1 + 2)  # Example of overloading
print('a' + 'b')
print(emp_1)  # Vague representation of class if __str__ not defined
print(repr(emp_1))  # String needed to reproduce object
print(str(emp_1))  # String representing the object itself
print(emp_1.__repr__())  # Same as above
print(emp_1.__str__())
print("\nAdd functions below\n")
print(1 + 2)
print(int.__add__(1, 2))  # Same as above
print(str.__add__('a', 'b'))
print(emp_1 + emp_2)  # Overloaded via __add__
print("\nlen functions below\n")
print(len('test'))
print('test'.__len__())  # Same as above
print(len(emp_1))  # Full name length
