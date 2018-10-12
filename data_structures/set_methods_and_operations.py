# References https://www.youtube.com/watch?v=r3R3h5ly_8g
# References https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Python-Sets
# A set is a list without duplicate values
# Has extra useful methods
# Can use intersection, difference, union with other sets
# O(n) to check if value in list
# O(1) to check if value in set

s1 = set([1, 2, 3, 4, 5, 1, 2, 3])  # Removes duplicates
# s1 = set{1, 2, 3, 4, 5}  # Same result as above
# Do not use s1 = {}, this makes a dictionary
empty_set = set([])
not_set = {}  # Actually makes a dictionary
print(s1)
print(empty_set)
print(not_set)
print("\nAdd/update values below\n")
s1.add(6)
s1.update([6, 7, 8])  # Extracts and puts in set
s2 = set([8, 9, 10])
s1.update(s2)  # Extracts elements and puts in set
print(s1)
print("\nRemove/discard values below\n")
s1.remove(5)
# s1.remove(5)  # If ran again, would crash
s1.discard(5)  # Does not crash if not in set
print(s1)
print("\nSet operations below\n")
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = set([3, 4, 5])
s4 = s1.intersection(s2, s3)
s5 = s1.difference(s2)  # What's in s1 that's not in s2
s6 = s2.difference(s1)  # What's in s2 that's not in s1
s7 = s2.difference(s1, s3)  # What's in s2 thats not in s1 or s3
print(s4)
print(s5)
print(s6)
print(s7)  # Empty set, s2 has elems from s1 and s2
print("\nSymmetric differences\n")
# Elements that are not in both s1 and in s2
s4 = s1.symmetric_difference(s2)  # Same if were to swap s1 and s2
print(s4)
print("\nLists versus sets\n")
l1 = [1, 2, 3, 1, 2, 3]  # List with duplicates
l2 = list(set(l1))  # Removes duplicates and re-casts
print(l1)
print(l2)
print("\nAdditional operations\n")
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']
# Okay to pass in developers as a list, but first argument must be set
result = set(gym_members).intersection(developers)
print(result)  # Developers who have gym memberships
result = set(employees).difference(gym_members, developers)
print(result)  # Employees who aren't developers or gym members
print("\nMembership tests\n")
if 'Corey' in developers:
    print('Found!')  # Faster to perform on set than on list O(1)
