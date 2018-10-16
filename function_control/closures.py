# References https://www.youtube.com/watch?v=swU3c34d2NQ
# A closure is a record storing a function together with an
# environment: a mapping associating each free variable of the function
# with the value or storage location to which the name was bound when
# the closure was created. A closure, unlike a plain function, allows
# the function to access those captured variables through the closure's
# reference to them, even when the function is invoked outside their
# scope.
# From Corey:
# A closure is an inner function that remembers and has access to
# variables in the local scope in which it was created even after the
# outer function has finished executing. A closure closes over the free
# variables from their environment.


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Return the return of a function, using parenthesis")


def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)  # message is a "free variable"

    return inner_func()


outer_func()

new_section("Return a function, excluding parenthesis")


def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)  # message is a "free variable"

    return inner_func


my_func = outer_func()
print("print my_func:", my_func)
print("print my_func.__name__:", my_func.__name__)
my_func()

new_section("Return a function, excluding parenthesis")


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)  # message is a "free variable"

    return inner_func


hi_func = outer_func('Hi')
hello_func = outer_func('Hello')
print("print hi_func:", hi_func)
print("print hello_func:", hello_func)
print("Running functions below")
hi_func()
hello_func()

new_section("Logging function")
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):  # Takes in any number of arguments
        logging.info(
            f"Running '{func.__name__}' with arguments {args}")
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

print("See example.log")