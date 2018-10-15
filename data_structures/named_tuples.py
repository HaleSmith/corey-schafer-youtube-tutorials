# References https://www.youtube.com/watch?v=GfxJYp9_nJA
# Named tuples like tuples but more readable
# Is like a compromise between tuple and dict
# Note syntax has been updated since video made

from collections import namedtuple

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Accessing value in a tuple")
color = (55, 155, 255)  # RGB, but not very readable
print(color[0])

new_section("Accessing value in dict representation")
color = {'red': 55, 'green': 155, 'blue': 255}
print(color['red'])  # But dict isn't immutable

new_section("Defining a named tuple")
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
print(color[0])
print(color.red)
# Can define out of order, if explicit
color = Color(blue=255, red=55, green=155)
print(color.green)