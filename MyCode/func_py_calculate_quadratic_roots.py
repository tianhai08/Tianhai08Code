# func_py_calculate_quadratic_roots.py
import math

def func_py_calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        return None

print(func_py_calculate_quadratic_roots(1, -7, 12))
