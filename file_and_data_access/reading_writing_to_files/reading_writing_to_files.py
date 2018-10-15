# References https://www.youtube.com/watch?v=Uh2ebFW8OYM
# References https://docs.python.org/3/library/functions.html#open
# Context managers will automatically close file
# 'w' will overwrite a file that already exists
# If in 'w' and seek to 0, will overwrite as much as is needed
# 'a' will append to a file that already exists
# Use binary mode to read/write bytes instead of text


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section(f"Using the open() command (not recommended)")
# Defaults to open it for reading, but specify via second argument
# 'w' for write, 'a' for append, 'r+' for read/write
f = open('test.txt', 'r')  # In same directory
print(f"Filename: {f.name}")
print(f"File mode: {f.mode}")
f.close()  # Need to close file when done


new_section(f"Using context manager to open files (recommended)")
with open('test.txt', 'r') as f:
    f_contents = f.read()  # Loading this works when data is small
    print(f_contents)
# Still have access to the context afterwards, but file is closed
print(f"File closed: {f.closed}")

new_section(f"Using readlines function")
with open('test.txt', 'r') as f:
    f_contents = f.readline()  # Just one line, takes next in file
    print(f_contents, end='')  # Print without a newline afterwards
    f_contents = f.readlines()  # Shows remaining lines with breaks
    print(f_contents)

new_section(f"Using for line in f")
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
    print()

# Read will return an empty string after all data has been read
new_section(f"Using read with a size argument, * as separator")
with open('test.txt', 'r') as f:
    size_to_read = 15
    f_contents = f.read(size_to_read)  # Picks up where it left off
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
    print()

new_section(f"Using file.tell()")
with open('test.txt', 'r') as f:
    size_to_read = 15
    print(f"Position in file before read: {f.tell()}")
    f_contents = f.read(size_to_read)  # Picks up where it left off
    print(f"Position in file after read: {f.tell()}")

new_section(f"Using file.seek()")
with open('test.txt', 'r') as f:
    size_to_read = 15
    f_contents = f.read(size_to_read)
    print(f_contents, end='*')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents)

new_section(f"Trying to write to a file opened in read mode")
with open('test.txt', 'r') as f:
    try:
        f.write('Test')
    except Exception as e:
        print(f"Exception: {e} in {__name__}")

# May need to delete test2.txt to demonstrate
new_section(f"Creating a new file without actually writing to it")
with open('test2.txt', 'w') as f:
    pass  # Created file even though doesn't exist
print("See test2.txt")

new_section(f"Writing twice to an existing file")
with open('test3.txt', 'w') as f:
    f.write('Test')
    f.write('Test')  # Wrote twice
print("See test3.txt")

new_section(f"Overwriting an existing file with seek")
with open('test4.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')  # Wrote twice
print("See test4.txt")

new_section(f"Copying data from a file into another file")
with open('test.txt', 'r') as rf:  # Open as a readfile
    with open('test_copy.txt', 'w') as wf:  # Open as writefile
        for line in rf:
            wf.write(line)
print("See test2_copy.txt")

new_section(f"Copying a picture file using binary mode")
with open('gsu75.jpg', 'rb') as rf:  # 'rb' read binary mode
    with open('gsu75_copy.jpg', 'wb') as wf:  # 'wb' write binary mode
        for line in rf:
            wf.write(line)
print("See gsu75_copy.txt")

new_section(f"Image copy using chunk size")
with open('gsu75.jpg', 'rb') as rf:  # 'rb' read binary mode
    with open('gsu75_copy2.jpg', 'wb') as wf:  # 'wb' write binary mode
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
print("See gsu75_copy2.txt")