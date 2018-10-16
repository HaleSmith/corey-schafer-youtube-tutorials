# References https://www.youtube.com/watch?v=x3v9zMX1s4s
# Assume that if walks and talks like duck, should treat like duck
# Don't care what type of object working with
# Just care that object can do what is requested
# EAFP doesn't consume memory doing error checking

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Non-pythonic example")
class Duck:
    def quack(self):
        print("Quack, quack")
    def fly(self):
        print("Flap, flap!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")
    def fly(self):
        print("I'm flapping my arms!")

def quack_and_fly(thing):
    """Example of non-duck typed code"""
    if isinstance(thing, Duck):  #
        thing.quack()
        thing.fly()
    else:
        print("This has to be a duck!")

d = Duck()
quack_and_fly(d)
print()
p = Person()
quack_and_fly(p)  # Person is still able to quack and fly

new_section("Pythonic example, no error checking")
def quack_and_fly(thing):
    """Example of duck typed code"""
    thing.quack()
    thing.fly()

quack_and_fly(d)
print()
quack_and_fly(p)

new_section("Non Pythonic example, too much error checking")
def quack_and_fly(thing):
    """Look before you leap (LBYL) excessive error checking"""
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

quack_and_fly(d)
print()
quack_and_fly(p)

new_section("EAFP example")
def quack_and_fly(thing):
    """Try to perform actions and make exception if necessary"""
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(f"In {__name__}: {e}")

quack_and_fly(d)
print()
quack_and_fly(p)

new_section("Dictionary example, non-pythonic")
person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print("Missing some keys")
person = {'name': 'Jess', 'age': 23}
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print("Missing some keys")

new_section("Dictionary example, Pythonic")
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print(f"In {__name__}: Missing key {e}")

new_section("List example, non-Pythonic")
my_list = [1, 2, 3, 4, 5]
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index doesn't exist")

new_section("List example, Pythonic")
try:
    print(my_list[5])
except IndexError:
    print("Index doesn't exist")

new_section("Race condition")
import os
my_file = "/tmp/test.txt"

# Maybe heck returns true, but in short time file becomes unavailable
# Is a "race" to then open file as f
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print("File can't be accessed")

new_section("Pythonic no-race condition")
try:
    f = open(my_file)
except IOError as e:
    print("Can't access file")
else:
    with f:
        print(f.read())


