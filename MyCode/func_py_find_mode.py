# func_py_find_mode.py
from collections import Counter

def func_py_find_mode(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

print(func_py_find_mode([10, 20, 30, 30, 40, 50]))
