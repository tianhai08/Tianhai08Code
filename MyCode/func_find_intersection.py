# func_find_intersection.py
def func_find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(func_find_intersection([1, 2, 3], [2, 3, 4]))
