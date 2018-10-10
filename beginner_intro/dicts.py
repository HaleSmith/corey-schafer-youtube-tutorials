# AKA hash maps or associative arrays
# Keys can be immutable data types
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])
# Will throw error if key doesn't exist
# print(student['phone'])

print(student.get('name', 'Not Found'))
print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student.get('phone', 'Not Found'))
print(student)

student.update({'name': 'Phil', 'age': 26, 'phone': '444-4444'})
print(student)

del student['age']
print(student)

phone = student.pop('phone')
print(student, phone)

student.update({'name': 'Phil', 'age': 26, 'phone': '444-4444'})
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():  # Loop over all elements
    print(key, value)
