# References https://www.youtube.com/watch?v=nghuHvKLhJA
# Format codes at https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# In Python 3.6 and above

first_name = 'Corey'
last_name = 'Schafer'

# Old way of strings
sentence = "My name is {} {}".format(first_name, last_name)
print(sentence)
# Python 3.6 and above allows functions inside {}
sentence = f"My name is {first_name.upper()} {last_name.lower()}"
print(sentence)
print("\nDictionary example below\n")
person = {'name': 'Jenn', 'age': 23}
sentence = "My name is {} and I am {} years old".format(person['name'],
                                                        person['age'])
# Need special quotes handling - can't use double quotes below
# Could do with escape sequences, or with ' inside of ""
sentence2 = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

print("\nCalculation example below\n")
calculation = f"4 times 11 is equal to {4 * 11}"
print(calculation)
for n in range(7, 11):
    # Zero padding and 2 digits long
    sentence = f"The value is {n:02}"
    print(sentence)

print("\nMore formatting\n")
pi = 3.14159265
sentence = f"Pi is equal to {pi}"
print(sentence)
# After the decimal, print to 4 digits for this float, also rounds
sentence = f"Pi is equal to {pi:.4f}"
print(sentence)

print("\nDates\n")
from datetime import datetime
birthday = datetime(1994, 6, 19)
sentence = f"Someone has a birthday on {birthday}"
print(sentence)  # Not cleanly formatted
sentence = f"Someone has a birthday on {birthday:%B %d, %Y}"
print(sentence)  # Cleanly formatted