# References https://www.youtube.com/watch?v=D3JvDWO-BY4

print("\nLists below\n")
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)  # Returns a new sorted list
print(s_li)  # Sorted in ascending order
print(li)  # Original is left unsorted
li.sort()  # Returns None, sorts in place, works specifically on list
print(li)  # Now is sorted in place
s_rev = sorted(li, reverse=True)
print(s_rev)  # Reverse sorted, also works for sort method
print("\nTuples and dicts below\n")
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)  # Converts the values to a list and returns
print(s_tup)
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)  # Returns list of sorted keys
print(s_di)
print("\nNegative sort below\n")
li = [-6, -5, -4, 1, 2, 3]
print(li)
s_li = sorted(li)  # Most negative values appear first
print(s_li)
# Runs each element through abs value function before sorting
s_abs = sorted(li, key=abs)
print(s_abs)
print("\nObject sort below via key function")
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.salary}"

    @classmethod  # Alternative constructor via class method
    # 'from' is common convention for naming - from_array, etc.
    # See datetime.py (common library) for examples
    def from_string(cls, emp_str):
        # Data is in string form
        name, age, salary = emp_str.split(', ')
        age, salary = int(age), int(salary)
        return cls(name, age, salary)

e1 = Employee('Carl', 37, 70000)
carl_string = repr(e1)
e1 = Employee.from_string(carl_string)  # For practice
print(repr(e1))
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employees = [e1, e2, e3]
print(employees)
def e_sort(emp):
    return emp.name
s_employees = sorted(employees, key=e_sort)
print(s_employees)
print("\nObject sort below via lambda/attrgetter function")
# Lambda is quick anonymous function, sort on instance.name field
s_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
print(s_employees)
from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)

