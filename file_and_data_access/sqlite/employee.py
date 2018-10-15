# Taken from https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-SQLite/employee.py
# For use with sqlite_demo.py

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
