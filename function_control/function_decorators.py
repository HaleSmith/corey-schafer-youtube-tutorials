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

# Resume for pause at 17:55
