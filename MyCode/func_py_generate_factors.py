# func_py_generate_factors.py
def func_py_generate_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(func_py_generate_factors(30))
