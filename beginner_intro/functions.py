# From https://www.youtube.com/watch?v=9Os0o3wzS_I# Snippets atdef stub_func():    pass  # Allows a stub definition to be defined without errorsprint(stub_func)  # Prints memory address of the functionprint(stub_func())  # Prints output of functiondef hello_func():    return "Hello Function!"print(hello_func())print(hello_func().upper())  # Apply method to function return string# Can re-define a function (defined above)# Uses default argument for name (keyword argument)# Positional arguments must come before keyword argumentsdef hello_func(greeting, name='You'):    return f"{greeting}, {name}."  # Uses new f-string functionality    # return '{} Function.'.format(greeting) would have worked tooprint(hello_func('Aloha'))print(hello_func('Aloha', 'Corey'))# Can accept arbitrary number of positional or keyword arguments# Args are a tuple, and kwargs are a dictionarydef student_info(*args, **kwargs):    print(args)    print(kwargs)student_info('Math', 'Art', name='John', age=22)courses = ['Math', 'Art']info = {'name': 'John', 'age': 22}# Unpacks the list and the dictionary and passes in individuallystudent_info(*courses, **info)# Number of days per month. First value placeholder for# indexing purposes.month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]def is_leap(year):    """Return True for leap years, False for non-leap years."""    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)def days_in_month(year, month):    """Return number of days in that month in that year."""    if not 1 <= month <= 12:        return 'Invalid Month'  # Can return a string or an int    if month == 2 and is_leap(year):        return 29    return month_days[month]print(is_leap(2017))print(is_leap(2016))print(days_in_month(2017, 2))