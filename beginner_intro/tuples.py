empty_tuple = ()
empty_tuple = tuple()

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']  # A list
list_2 = list_1  # Both lists are the same mutable object

print(list_1)
print(list_2)

list_1[0] = 'Art'  # Modifies both lists

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')  # A tuple
tuple_2 = tuple_1  # A copy of the tuples

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # Can not do this, tuples are immutable

print(tuple_1)
print(tuple_2)
