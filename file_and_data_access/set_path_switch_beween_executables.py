# References https://www.youtube.com/watch?v=OdIHeg4jj2c


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Command prompt notes")
# First command
# C:\Users\kahna\AppData\Local\Programs\Python\Python37-32\Python

# Path variable
# Control panel->System->Advanced system settings->Environment Vars
# Click user variables section at top
# Click path then edit
# Rearrange so that python 3 dir at top
# Did not change because testing scripts were in v2.7.3...
# Pip, etc. is in scripts folder
# sys.executable shows the currently running python.exe (in >>>)
# echo %path% shows evironment vars (in console)
# Pip and python are in separate places
# Pip install django command in console:
# C:\Users\kahna\AppData\Local\Programs\Python\Python37-32\Scripts\pip install Django
# This installed Django to the Scripts folder
# pip show (in console) shows the package
# pip show pip shows info on pip

new_section("Using sys commands in PyCharm")
import sys
print("Version: ", sys.version)
print("Executable: ", sys.executable)
# Virtual environment: separate executable, with packages, per project
