# References https://www.youtube.com/watch?v=K8L6KVGG-7o
# Raw string is a string prefixed with an r
# Don't handle backslashes in any special way
# See syntax_snippets.txt
# From beginning of video, emails.py is next, and picks up 46:32

import re

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


# Simple sample data (SSD)
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence = 'Start a sentence and then bring it to an end'

new_section("Raw strings")
print("Non-raw string:", '\tTab')
print("Raw string:", r'\tTab')

new_section("re.compile case-sensitive search")
pattern = re.compile(r'abc')  # Pattern with actual abc text
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)  # Span is beginning and end of the text
print("Printing indices from match: ", text_to_search[1:4])
pattern = re.compile(r'cba')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)  # No matches print

new_section("meta-character example")
# Period matches all text styles
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)
print("Print matches for unescaped '.':")
for i, match in enumerate(matches):
    print(match)
    if i > 2:
        break  # Only print out 4 results
pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
print("Print matches for escaped '.' in a pattern:")
for match in enumerate(matches):
    print(match)

new_section("All 'ha's with a word boundary before")
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in enumerate(matches):
    print(match)
print('text_to_search[66:71: ', text_to_search[66:71])

new_section("Using string anchors")
pattern = re.compile(r'^sentence')
matches = pattern.finditer(sentence)
print("No match at beginning:")
for match in enumerate(matches):
    print(match)
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
print("Match at beginning:")
for match in enumerate(matches):
    print(match)

new_section("Extracting phone numbers")
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in enumerate(matches):
    print(match)

new_section("Reading from file")
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    print("Printing first several matches")
    for i, match in enumerate(matches):
        print(match)
        if i > 2:
            break

new_section("Matching phone numbers only separated by - or ., not *")
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in enumerate(matches):
    print(match)

new_section("Only match 800/900 numbers")
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in enumerate(matches):
    print(match)

new_section("Matching a range of numbers between 1 and 5")
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)
for i, match in enumerate(matches):
    print(match)
    if i > 2:
        break

new_section("Matching a range of letters between a and z and A-Z")
pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(text_to_search)
for i, match in enumerate(matches):
    print(match)
    if i > 2:
        break

new_section("Matching values not in character set")
pattern = re.compile(r'[^a-zA-Z]')  # ^ means not in set
matches = pattern.finditer(text_to_search)
for i, match in enumerate(matches):
    print(match)
    if i > 2:
        break

new_section("Using quantifiers")
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for i, match in enumerate(matches):
    print(match)
    if i > 2:
        break

new_section("Names with Mr")
# 'Mr' Followed by 1 or 0 '.', followed by space, followed by uppercase
# letter, followed by 0 or more word characters
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for i, match in enumerate(matches):
    print(match)

new_section("Matching all names via a group")
# Same as above, but M can be followed by 'r', 's', or 'rs'
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for i, match in enumerate(matches):
    print(match)

new_section("pattern.findall method for increased efficiency")
# Find iter will return additional info
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# findall with only extract the relevant groups
# Returns a tuple if more than one group is specified
matches = pattern.findall(text_to_search)
print("Matched groups from pattern only")
for match in (matches):
    print(match)
print("Showing all matches without extra object info")
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.findall(text_to_search)
for match in (matches):
    print(match)

new_section("pattern.match to find just at the beginning of sentence")
# Returns None if no match found, doesn't return an iterable
pattern = re.compile(r'Start')
match = pattern.match(sentence)
print("Match for 'Start': ", match)
pattern = re.compile(r'sentence')
match = pattern.match(sentence)
print("Match for 'sentence': ", match)

new_section("pattern.search to find anywhere in a string")
pattern = re.compile(r'sentence')
match = pattern.search(sentence)
print("Search for 'sentence': ", match)

new_section("Flags to create a pattern where set can be uppers or lowers")
# Ignore the case of the letter
pattern = re.compile(r'start', re.IGNORECASE)  # Equivalent to re.I
match = pattern.search(sentence)
print("Search for 'start': ", match)