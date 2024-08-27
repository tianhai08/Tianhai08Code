# func_py_find_harshad_numbers.py
def func_py_find_harshad_numbers(limit):
    return [n for n in range(1, limit) if n % sum(int(digit) for digit in str(n)) == 0]

print(func_py_find_harshad_numbers(100))
