# fun_py_find_median_of_list.py
def fun_py_find_median_of_list(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

print(fun_py_find_median_of_list([3, 1, 4, 1, 5, 9, 2]))
