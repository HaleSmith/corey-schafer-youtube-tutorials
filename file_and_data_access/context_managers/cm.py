# References https://www.youtube.com/watch?v=-aKFBoZpiqA
# Context managers help with specifying resources
# CMs clean up setup/teardown process
# CMs also handle errors and still close if problem happens

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Without CM: must close when done")
f = open('sample.txt', 'w')
f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
f.close()
print("See sample.txt")

new_section("With CM: auto-closure performed")
with open('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
print("See sample.txt")

new_section("Defining and using a custom CM with a class")
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # the 'with' statement calls this code
    def __enter__(self):  # Setup
        self.file = open(self.filename, self.mode)
        # This returns the object listed after 'as'
        return self.file  # Returns object working with inside CM

    # This is called whenever the CM is exited via back-indentation
    def __exit__(self, exc_type, exc_val, traceback):  # Teardown
        self.file.close()

with Open_File('sample2.txt', 'w') as f:
    f.write('Testing')

print(f"Verify file closed outside CM: {f.closed}")
print("See sample2.txt")

new_section("Custom CM via contextmanager tag, lacking try/except")
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    # Everything before yield is equivalent to __enter__
    f = open(file, mode)
    # Yield is returning the object, where code in with statement runs
    yield f
    # Everything after yield is same as __exit__
    f.close()

with open_file('sample3.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f"Verify file closed outside CM: {f.closed}")
print("See sample3.txt")

new_section("Custom CM via contextmanager tag, with try/except")
@contextmanager
def open_file(file, mode):
    try:  # Setup
        # Everything before yield is equivalent to __enter__
        f = open(file, mode)
        # Yield is returning the object, where code in with statement runs
        yield f
    finally:  # Teardown
        # Everything after yield is same as __exit__
        f.close()

new_section("CD example without CM")
import os

cwd = os.getcwd()  # Current working directory
os.chdir('Sample-Dir-One')  # Change directory
print(f"Dir 1 contents: {os.listdir()}")
os.chdir(cwd)  # Change back to original directory

cwd = os.getcwd()  # Current working directory
os.chdir('Sample-Dir-Two')  # Change directory
print(f"Dir 2 contents: {os.listdir()}")
os.chdir(cwd)  # Change back to original directory

new_section("CD example with CM")
@contextmanager
def change_dir(destination):
    try:  # Setup
        cwd = os.getcwd()  # Current working directory
        os.chdir(destination)  # Change to destination
        yield  # Don't need to return anything
    finally:  # Executed no matter the results of try (teardown)
        os.chdir(cwd)  # Go back to original

with change_dir('Sample-Dir-One'):
    print(f"Dir 1 contents: {os.listdir()}")

with change_dir('Sample-Dir-Two'):
    print(f"Dir 2 contents: {os.listdir()}")