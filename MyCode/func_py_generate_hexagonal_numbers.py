# func_py_generate_hexagonal_numbers.py
def func_py_generate_hexagonal_numbers(limit):
    hexagonal_numbers = [n * (2 * n - 1) for n in range(1, limit + 1)]
    return hexagonal_numbers

print(func_py_generate_hexagonal_numbers(10))
