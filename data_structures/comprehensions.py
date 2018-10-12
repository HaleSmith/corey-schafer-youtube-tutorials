# References https://www.youtube.com/watch?v=3dt4OGnU5sM


# Separator for print output
def new_section(message):
    print(f"\n---{message}---\n")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nExample 1: Give 'n' for each 'n' in nums\n")
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

print("\nExample 2: Each n in nums with less syntax\n")
my_list = [n for n in nums]
print(my_list)

print("\nExample 3: 'n*n' for each n in nums\n")
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

new_section("Example 4: n^2 via comprehension syntax")
my_list = [n*n for n in nums]
print(my_list)

new_section("Maps and lambdas")
# Runs through an anonymous function lambda
my_list = map(lambda num: num*num, nums)  # Doesn't work that well
print(my_list)

new_section("n in nums if n is even")
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

new_section("n in nums if n is even via comprehensions")
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

new_section("filter and lambda function for n if even")
# Tutorial does not return an address, but rather same as above
my_list = filter(lambda n: n % 2 == 0, nums)  # Returns an address
print(my_list)

new_section("Multi list comprehensions via loop")
# A letter number pair for each letter in abcd and num in 0123
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

new_section("Multi list comprehensions without loop")
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

new_section("Dictionary comprehension with loop")
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# Prints object address, but in tutorial printed a list of tuples
print(str(zip(names, heroes)))
my_dict = {}
# Zip merges lists together into tuples
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)

new_section("Dictionary comprehension without loop and not including Peter")
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

new_section("Set comprehensions via loop")
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

new_section("Set comprehensions without loop")
my_set = {n for n in nums}
print(my_set)

new_section("Generator expressions via loop")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n*n


my_gen = gen_func(nums)
for i in my_gen:
    print(i)

del gen_func, my_gen
new_section("Generator expression via reduced syntax")

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)