# References https://www.youtube.com/watch?v=jCzT9XFZ5bw

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)  # Not updated when attribute manually set
print(emp_1.fullname())
print("\nUpdating class definition without decorator\n")
del Employee, emp_1


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Will auto-update if first or last are set
    # However, implementing this will require others to change code
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email())  # Now need parenthesis
print(emp_1.fullname())
emp_1.first = 'Jim'
print(emp_1.first)
# Updates when attribute changed manually, but need ()
print(emp_1.email())
print(emp_1.fullname())

print("\nUpdating class definition including decorator\n")
del Employee, emp_1


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Lets attribute be auto-updated function of other attributes
    # Don't need to call emp_1.email()
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # Changes from this method will cascade to the above attributes
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
print(emp_1.email)
print(emp_1.fullname)
emp_1.first = 'Joe'
print(emp_1.email)
print(emp_1.fullname)
emp_1.fullname = 'Corey Schafer'
print(emp_1.fullname)
print(emp_1.email)
del emp_1.fullname
print(emp_1.fullname)
