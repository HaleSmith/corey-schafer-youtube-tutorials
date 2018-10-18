# References https://www.youtube.com/watch?v=K8L6KVGG-7o

import re


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

new_section("Any number of letters, @, any number of letters, .com")
pattern = re.compile(r'[a-zA-z]+@[a-zA-Z]+\.com')
matches = pattern.finditer(emails)
for match in matches:
    print(match)

new_section("Add in allowing of '.' and edu")
pattern = re.compile(r'[a-zA-z.]+@[a-zA-Z]+\.(com|edu)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)

new_section("Add in allowing of hyphens and numbers")
pattern = re.compile(r'[a-zA-z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)

new_section("Dissecting email parsing regex pattern")
# First character set matches all lowers, all uppers, all digits, an
# underscore, a plus, or a hyphen, for 1 or more characters
# Then '@'
# Second character set matches all lowers, all uppers, all digits, or
# a hyphen, for 1 or more characters
# Then escaped '.'
# Then another character set for all lowers, uppers, nums, hyphen, dot,
# for 1 or more characters
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)
for match in matches:
    print(match)