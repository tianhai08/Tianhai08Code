# func_py_find_polygonal_numbers.py
def func_py_find_polygonal_numbers(sides, limit):
    return [n * ((sides - 2) * n - (sides - 4)) // 2 for n in range(1, limit + 1)]

print(func_py_find_polygonal_numbers(5, 10))
