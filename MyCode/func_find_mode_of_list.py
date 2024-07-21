# func_find_mode_of_list.py
from collections import Counter

def func_find_mode_of_list(lst):
    count = Counter(lst)
    return max(count, key=count.get)

print(func_find_mode_of_list([5, 3, 9, 1, 4, 4, 9, 4]))
