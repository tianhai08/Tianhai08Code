# func_py_check_leap_year.py
def func_py_check_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

print(func_py_check_leap_year(2024))
