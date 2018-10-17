# References https://www.youtube.com/watch?v=QVdf0LgmICw
# Local, enclosing, global, built-in (LEGB)
# Local is variables defined within a function
# Enclosing are variable inside local scope of enclosing function
# Global are defined at top level of a module or declared global
# Built-ins are preassigned in Python
# LEGB is an order of precedence

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Accessing a global variable")

x = "global x"  # Global because in main body of file


def test():
    x = "local x"  # now local to this function
    y = "local y"  # y is local to this function
    print(y, "from inside test")
    print(x, "from inside test")


print(x, "from outside test")
test()
try:
    print(y)
except Exception as e:
    print("Unable to print y: ", e)
del x, test

new_section("Overwriting a previous global variable")

x = "global x"  # Global because in main body of file


def test():
    global x  # Now working with a global variable (in this module)
    x = "local x"
    print(x, "from inside test")


test()
print(x, "from outside test")
del x, test

new_section("Working with function arguments")


def test(z):  # z is now local to the function
    print(z, "from inside test")

test("Local z")
try:
    print(z)
except NameError as e:
    print("Unable to print z: ", type(e))
del test

new_section("Built-in scope example")
m = min([5, 1, 4, 2, 3])  # min is a built in
print("results of min():", m)

new_section("Modifying built-ins")
import builtins
print("dir(builtins):", dir(builtins))


def min():  # Overwriting a builtin
    pass

try:
    m = min([5, 1, 4, 2, 3])
except Exception as e:
    print("\nUnable to get min: ", type(e), ':', e)
del min  # Re-import to correct the problem
import builtins
m = min([5, 1, 4, 2, 3])
print("After re-import, m = ", m)

new_section("Enclosing functions")
# Simple example of scope
x = "global x"


def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
print(x)
del outer

new_section("Non local keyword")
# Modifying the enclosing variable


def outer():
    x = "outer x"
    print("Before inner, x = ", x)

    def inner():
        nonlocal x
        x = "inner x"
        print("During inner, x = ", x)

    inner()
    print("After inner, x = ", x)

outer()
