# References https://www.youtube.com/watch?v=ve2pmm5JqmI

import os


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Get into sample directory")
os.chdir('sample_directory')
print("Current directory: ", os.getcwd())
print("Directory contents: ")
for f in os.listdir():
    print(f)

new_section("Split off extension of file and return tuple")
for f in os.listdir():
    # splitext splits off file extension
    print(os.path.splitext(f), end=', file_name: ')
    file_name, file_ext = os.path.splitext(f)
    print(file_name)

new_section("Split off name via hyphen")
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))

new_section("Reformat string with elements")
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()  # Splits off whitespace on left or right
    # Leaves off '#' at beginning, and then pads with 0 to two digits
    f_num = f_num.strip()[1:].zfill(2)
    print(f"{f_num}-{f_title}{f_ext}")

new_section("Reassign file names. See sample_directory")
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = f"{f_num}-{f_title}{f_ext}"
    os.rename(f, new_name)