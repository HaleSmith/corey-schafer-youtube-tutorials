# References https://www.youtube.com/watch?v=5cvM-crlDvg
# References https://docs.python.org/2/library/functions.html#str
# References https://docs.python.org/2/library/functions.html#repr
# The goal of __repr__ is to be unambiguous
# The goal of __str__ is to be readable
# Passing to eval means the string should pass as a command
# Can use repr to test what and object is

a = [1, 2, 3, 4]
b = "sample string"

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

import datetime
a = datetime.datetime.utcnow()
b = str(a)

print(f"str(a): {str(a)}")
print(f"str(b): {str(b)}\n")
print(f"repr(a): {repr(a)}")
print(f"repr(b): {repr(b)}\n")
