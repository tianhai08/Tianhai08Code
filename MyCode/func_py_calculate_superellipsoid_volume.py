# func_py_calculate_superellipsoid_volume.py
import math

def func_py_calculate_superellipsoid_volume(a, b, c, n):
    return (2 * math.gamma(1 + 1/n)**3 / math.gamma(1 + 3/n)) * a * b * c

print(func_py_calculate_superellipsoid_volume(3, 4, 5, 2))
