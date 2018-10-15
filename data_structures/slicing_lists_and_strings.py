# References https://www.youtube.com/watch?v=ajrtAuDg3yw
# Lists of form list[start:end:step]
# Start index is inclusive
# End index is non-inclusive even in reverse

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_section("Accessing indices")
print(f"List: {my_list}, 0-indexed")
print(f"Value at index 5: {my_list[5]}")
print(f"Value at index -2: {my_list[-2]}")
print(f"From index 2 to 7: {my_list[2:7]}")
print(f"From index -7 to -2: {my_list[-7:-2]}")

new_section("Accessing end/start via ':'")
print(f"List from 1 until end: {my_list[1:]}")
print(f"List from start until -1: {my_list[:-1]}")
print(f"Entire list: {my_list[:]}")

new_section("Specifying step size ':'")
print(f"Every other value from index 2 to 8: {my_list[2:-1:2]}")
# Note that 1 is now the end index and is non-inclusive
print(f"Negative step size from 8 to 2: {my_list[-2:1:-1]}")
print(f"Whole list backwards: {my_list[::-1]}")

new_section("Slicing strings")
sample_url = 'http://coreyms.com'
print(f"url: {sample_url}")
print(f"Reverse url: {sample_url[::-1]}")
print(f"Top level domain: {sample_url[-4:]}")
print(f"Without http:// : {sample_url[7:]}")
print(f"Without http or .com : {sample_url[7:-4]}")