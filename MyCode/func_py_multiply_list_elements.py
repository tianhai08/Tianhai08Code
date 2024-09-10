# func_py_multiply_list_elements.py
def func_py_multiply_list_elements(lst):
    result = 1
    for x in lst:
        result *= x
    return result

print(func_py_multiply_list_elements([2, 3, 4]))
