courses = ['History', 'Math', 'Physics', 'CompSci']  # A list
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
courses.remove('Math')
popped = courses.pop()
# sorted(list) doesn't sort in place
print(sorted(courses), courses, popped)

nums = [1, 5, 2, 4, 3]
nums.sort(reverse=True)  # Sorts in place
print(nums)


# Also len(list), list[-1:], list.insert(index, value), list.extend(list),
# list.extend(value)
