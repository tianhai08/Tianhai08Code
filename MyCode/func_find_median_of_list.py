# func_find_median_of_list.py
def func_find_median_of_list(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[length // 2]

print(func_find_median_of_list([1, 2, 3, 4, 5]))
