# func_py_calculate_triangle_area_herons.py
import math

def func_py_calculate_triangle_area_herons(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print(func_py_calculate_triangle_area_herons(3, 4, 5))
