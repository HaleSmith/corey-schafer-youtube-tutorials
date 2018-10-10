empty_list = []
empty_list = list()

courses = ['History', 'Math', 'Physics', 'CompSci']  # A list
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
courses.remove('Math')
popped = courses.pop()
print(sorted(courses), courses, popped)  # sorted(list) doesn't sort in place
print(courses.index('CompSci'))
print('Geography' in courses)
# enumerate(list) returns two values
for index, course in enumerate(courses, start=1):
    print(index, course)
course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)

nums = [1, 5, 2, 4, 3]
nums.sort(reverse=True)  # Sorts in place
print(nums)
print(sum(nums))
print(min(nums))
print(max(nums))

# Also len(list), list[-1:], list.insert(index, value), list.extend(list),
# list.extend(value)
