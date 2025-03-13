# func_py_string_permutations.py
from itertools import permutations

def func_py_string_permutations(s):
    return ["".join(p) for p in permutations(s)]

print(func_py_string_permutations("abc"))
