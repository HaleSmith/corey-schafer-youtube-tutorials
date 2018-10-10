# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

language = 'Python'

if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java")
elif language == 'JavaScript':  # No switch/case in Python
    print("Language is JavaScript")
else:
    print("No match")

# and, or, not are boolean operators
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credentials')

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

# Object type testing
# 'is' is the same as id(a) == id(b)
a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(a == b)
print(a is b)
print(b is c)
print(id(a), id(b), id(c))

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0.00001
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
