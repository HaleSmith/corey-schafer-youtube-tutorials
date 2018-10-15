# References https://www.youtube.com/watch?v=tJxcKyFMTGo
# Allows interface with OS - navigate file system, etc.

import os  # Built in module
from datetime import datetime

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Results of print(dir(os)): attributes/methods available")
print(dir(os))

new_section("Making a new folder via mkdir")
#os.mkdir('test')  # Could have done with makedirs too
print("See folder test")

new_section("Making nested folders via mkdirs")
#os.makedirs('test2/test3')
print("See folder test 2")

# new_section("Removing directories")
# os.rmdir('test4')  # Could also have used removedirs

# new_section("Renaming files")
# os.rename('demo.txt', 'demo2.txt')

new_section("Switching and printing directory")
print(f"Current directory: {os.getcwd()}")
print("Switching directory 2 up")
# os.chdir('../..')  # Path as a string
print(f"Current directory: {os.getcwd()}")

new_section("Contents enumeration")
print(f"Contents of current directory: {os.listdir()}")

new_section("os.stat() results")
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_size)  # Size in bytes
mod_time = os.stat('demo.txt').st_mtime  # Last modified
print(datetime.fromtimestamp(mod_time))

# Yields a tuple of path, dirs in path, and files in path
new_section("os.walk function")
# Go two files up
for dirpath, dirnames, filenames in os.walk('..'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames, end='\n\n')

new_section("os environment variables concatenation")
print(f"User home directory: {os.environ.get('HOME')}")
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(f"New filepath via path.join: {file_path}")

new_section("basename/dirname/split functions")
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))

new_section("Check existence/type")
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('../os_module'))
print(os.path.isfile('demo.txt'))

new_section("Split ext")
print(f"splitext result: {os.path.splitext('../os_module/demo.txt')}")