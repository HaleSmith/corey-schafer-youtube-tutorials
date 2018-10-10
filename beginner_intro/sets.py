not_empty_set = {}  # This creates a dict!
empty_set = set()


# Definition removes duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)  # Order is arbitrary, can change
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
