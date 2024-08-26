# func_py_find_bipartite_numbers.py
def func_py_find_bipartite_numbers(limit):
    return [n for n in range(1, limit) if sum(int(digit) for digit in str(n)) % 2 == 0]

print(func_py_find_bipartite_numbers(100))
