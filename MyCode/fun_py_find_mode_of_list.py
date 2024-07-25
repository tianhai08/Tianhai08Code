# fun_py_find_mode_of_list.py
from collections import Counter

def fun_py_find_mode_of_list(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

print(fun_py_find_mode_of_list([3, 1, 4, 1, 5, 9, 2, 2, 4]))
