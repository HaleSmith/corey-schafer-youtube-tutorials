# References https://www.youtube.com/watch?v=kr0mpwqttM0
# A programming language is said to have first-class functions if it treats
# functions as first-class citizens
# A first class citizen/object supports operations generally available to all
# other entities- be passed as an arg, returned from function, assigned to var
# Higher-order function pass and return functions


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Standard function definitions")


def square(x):
    return x * x


def cube(x):
    return x * x * x


f = square(5)
print(f"Printing the function: {square}")
print(f"Printing the return of function: {f}")
del f

new_section("Assigning a variable to a function")
f = square
# Both f and square have same location in memory
print(f"Printing the function: {square}")
print(f"Printing f: {f}")
print(f"Printing f(5): {f(5)}")

new_section("Passing a function as an argument")


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# Passing the function square as a variable
squares = my_map(square, [1, 2, 3, 4, 5])
print(f"Results of function with squares: {squares}")
cubes = my_map(cube, [1, 2, 3, 4, 5])
print(f"Results of function with cubes: {cubes}")

new_section("Returning a function")


# Returns a function that prints out the passed in message
def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('Hi!')  # Get the function that prints 'Hi!'
log_hi()  # Call the returned function

new_section("Somewhat practical example")


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1("Test Headline!")
print_h1("Another Headline!")

print_p = html_tag('p')
print_p("Test Paragraph!")