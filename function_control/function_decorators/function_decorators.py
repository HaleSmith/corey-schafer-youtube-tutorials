# References https://www.youtube.com/watch?v=FsAPt_9Bf3U


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Returning a function")


def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function  # Executes inner function


hi_func = outer_function('Hi')  # Assign a function
bye_func = outer_function('Bye')  # Assign a function
hi_func()  # Run the closure
bye_func()


new_section("Defining a decorator without tag")


def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function()
    return wrapper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)
decorated_display()

new_section("Defining a decorator with tag")


# Functional equivalent to above syntax
@decorator_function
def display():
    print("display function ran")


display()

new_section("More complex decorator")


# Need to be able to pass any number of positional or keyword arguments
# to wrapper and still have it execute
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display_info('John', 25)

new_section("Class decorator")


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call method executed this before "
              f"{self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_class  # Decorate the function with the class decorator
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display_info('John', '25')

new_section("Logging decorators")


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log",
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger  # Decorate the function with the logger
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display_info('A', '1')
display_info('B', '2')
display_info('C', '3')
print("See display_info.log")

new_section("Timing a function with a decorator")
import time


def my_timer(orig_func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


@my_timer
def display_info(name, age):
    time.sleep(0.1)
    print(f"display_info ran with arguments ({name}, {age})")


display_info('John', 25)

new_section("Chaining a decorator 1")
del display_info


@my_timer
@my_logger
def display_info(name, age):
    time.sleep(0.1)
    print(f"display_info ran with arguments ({name}, {age})")


# Note that the timer says that the "wrapper" ran in 1second
display_info('Hank', 30)

new_section("Chaining a decorator 2")
del display_info
del my_timer
del my_logger


def my_timer(orig_func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log",
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


# Note that the decorators have been flipped. This is like:
# display_info = my_logger(my_timer(display_info))
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(0.1)
    print(f"display_info ran with arguments ({name}, {age})")


# Outputs are different
display_info('Jerry', 40)

new_section("Single decorator name")
del display_info


def display_info(name, age):
    time.sleep(0.1)
    print(f"display_info ran with arguments ({name}, {age})")


display_info = my_timer(display_info)
print(display_info.__name__)

new_section("wraps decorator inside of a decorator")
from functools import wraps

del display_info


def display_info(name, age):
    time.sleep(0.1)
    print(f"display_info ran with arguments ({name}, {age})")


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log",
                        level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper

display_info = my_timer(display_info)
print(display_info.__name__)