# References https://www.youtube.com/watch?v=vTX3IwquFkc
# Format codes https://docs.python.org/3/library/time.html#time.strftime


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Conventional, but unreadable, concatenation")
person = {'name': 'Jenn', 'age': 23}
sentence = "My name is " + person['name'] + " and I am " + str(person['age']) \
    + " years old."
print(sentence)

new_section(".format option")
sentence = "My name is {} and I am {} years old.".format(person['name'],
                                                         person['age'])
print(sentence)

new_section(".format option with explicitly numbered placeholders")
sentence = "My name is {0} and I am {1} years old.".format(person['name'],
                                                           person['age'])

new_section(".format option with repeated placeholders")
tag = 'h1'
text = 'This is a headline'
sentence = "<{0}>{1}</{0}>".format(tag, text)  # Tag goes in twice
print(sentence)

new_section(".format option with passed in dictionary")
sentence = "My name is {0[name]} and I am {0[age]} years old." \
    .format(person)
print(sentence)

new_section(".format option with passed in list")
l = ['Jenn', '23']
sentence = "My name is {0[0]} and I am {0[1]} years old.".format(l)
print(sentence)

new_section("Printing out a class")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')
sentence = "My name is {0.name} and I am {0.age} years old.".format(p1)
print(sentence)

new_section("Formatting keyword arguments")
sentence = "My name is {name} and I am {age} years old.".format(name='Jenn',
                                                                age='30')
print(sentence)

new_section("Unpacking a dictionary via keyword arguments")
person = {'name': 'Jenn', 'age': 23}
sentence = "My name is {name} and I am {age} years old.".format(**person)
print(sentence)

new_section("Padding numbers")
for i in range(8, 12):
    # Pad with zeros, 2 digits long
    sentence = "The value is {:02}".format(i)
    print(sentence)

new_section("Decimal place formatting, with auto-rounding")
pi = 3.14159265
#  3 decimal places, for a float
sentence = "Pi is equal to {:.3f}".format(pi)
print(sentence)

new_section("Large number with comma separators")
# ** is exponentiation
# :, adds commas as separators
sentence = "1 MB is equal to {:,} bytes".format(1000**2)
print(sentence)

new_section("Chaining format options: commas, decimals")
sentence = "1 MB is equal to {:,.2f} bytes".format(1000**2)
print(sentence)

new_section("Dates and times formatting")
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(f"Raw datetime format: {my_date}")
print("Format code example below")
sentence = "{:%B %d, %Y}".format(my_date)
print(sentence)

new_section("Extracting additional date information")
# Uses 0 before colon because only one argument
sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day" \
           " of the year".format(my_date)
print(sentence)
