# References https://www.youtube.com/watch?v=K8L6KVGG-7o
# From 39:20 (in video) onward
# Top level domain refers to .com or .gov

import re


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

new_section("Extracting group information up until domain name")
# Match 'http', then 0 or 1 's', then '://', then optional 'www.'
pattern = re.compile(r'https?://(www\.)?')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

new_section("Continuing, onto domain name")
# Then one or more word characters up until the '.', then one or more
# word characters after the '.'
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

new_section("Extracting group information")
# Groups for 'www.', domain name, and top level name, each inside ()
# Group 0 is the entire match
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
print("Group 0, group 1, group 2, and group 3")
for match in matches:
    print(match.group(0), match.group(1), match.group(2), match.group(3))

new_section("Substituting group information")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# Back-reference group 2 then group 3. Replace a url with just the
# matched data from the patter
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)