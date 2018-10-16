# References https://www.youtube.com/watch?v=Dh-0lAyc3Bc
# In a for loop, should think of else as "no-break"


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Else in a for loop without break")
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)
else:  # Think of this as a no-break
    print("Hit the for/else statement")

new_section("Else in a for loop with break")
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)
    if i == 3:
        break
else:  # Think of this as a no-break
    print("Hit the for/else statement")

new_section("Else in a while loop without break")
i = 1
while i <= 5:
    print(i)
    i += 1
else:  # Think of this as a no-break
    print("Hit the for/else statement")

new_section("Else in a while loop with break")
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 4:
        break
else:  # Think of this as a no-break
    print("Hit the for/else statement")

new_section("Example: finding an index success")
def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i

my_list = ['Corey', 'Rick', 'John']
index_location = find_index(my_list, 'Rick')
print(f"Location of target is index: {index_location}")

new_section("Example: finding an index fail")
# Went through whole list and found nothing, so did else statement
index_location = find_index(my_list, 'Steve')
print(f"Location of target is index: {index_location}")