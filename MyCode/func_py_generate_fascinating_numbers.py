# func_py_generate_fascinating_numbers.py
def func_py_generate_fascinating_numbers(limit):
    fascinating_numbers = []
    for n in range(100, limit):
        concatenated = str(n) + str(n * 2) + str(n * 3)
        if ''.join(sorted(concatenated)) == '123456789':
            fascinating_numbers.append(n)
    return fascinating_numbers

print(func_py_generate_fascinating_numbers(1000))
