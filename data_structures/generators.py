# References https://www.youtube.com/watch?v=bD05uGo_sVI
# Generators don't hold the whole result in memory
# Generators only yield one result at a time
# Generator is high performing because doesn't hog memory


# Separator for print output
def new_section(message):
    print(f"\n---{message}---\n")


new_section("Square numbers generator via loop")


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)
del square_numbers

new_section("Square numbers generator via comprehension")


def square_numbers(nums):
    for i in nums:
        yield i*i

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)  # Prints a "generator object"
print(next(my_nums))  # Prints next item in generator
print(next(my_nums))  # Prints next item in generator
print(next(my_nums))  # Prints next item in generator
print(next(my_nums))  # Prints next item in generator
print(next(my_nums))  # Prints next item in generator (last item)

new_section("Generator extraction in a loop")
my_nums = square_numbers([1, 2, 3, 4, 5])
# Automatically stops when generator is empty
for num in my_nums:  # Won't throw a StopIteration exception
    print(num)

new_section("Square number generator via list comprehension")
# Creation of a list uses []
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)
# Creation of a generator uses ()
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)
for num in my_nums:
    print(num)

new_section("Convert a generator to a list")
my_nums = (x*x for x in [1, 2, 3, 4, 5])  # This is a generator
# Casting a generator to a list forces data into memory
print(list(my_nums))  # Reduces performance of a generator

new_section("Memory consumption demonstration")
print("See tutorial. List took 300MB, generator took 10KB")
