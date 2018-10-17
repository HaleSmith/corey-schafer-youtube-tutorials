# References https://www.youtube.com/watch?v=KlBPCzcQNU8


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Customizing the inputs to a decorator")


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)