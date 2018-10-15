# References https://www.youtube.com/watch?v=NIWwJbo-9_8


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Open without underscore")
try:
    f = open('testfile.txt')
except Exception as e:  # Can use to print the actual exception
    print(f"File exception: {e} in {__name__}")

new_section("Open with underscore but other exception present")
try:
    f = open('test_file.txt')
    var = bad_var  # This actually threw an error (bad_var not exist)
except FileNotFoundError as e:
    print(f"File exception: {e}")
except Exception as e:
    print(f"Another exception occurred: {e} in {__name__}")

new_section("Using the else clause when try code runs")
try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(f"File exception: {e}")
else:
    print(f"Contents of test_file.txt: {f.read()}")
    f.close()

new_section("Using the finally clause no matter what (1)")
try:
    f = open('testfile.txt')
except FileNotFoundError as e:
    print(f"File exception: {e}")
finally:  # Would be used to close down database, etc.
    print("Executing Finally")

new_section("Using the finally clause no matter what (2)")
try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(f"File exception: {e}")
else:
    print(f"Contents of test_file.txt: {f.read()}")
    f.close()
finally:  # Would be used to close down database, etc.
    print("Executing Finally")

new_section("Manually raising an exception")
try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except Exception as e:
    print(f"Exception: {e} in {__name__}")