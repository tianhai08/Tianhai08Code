# fun_most_frequent_element.py
def fun_most_frequent_element(lst):
    return max(set(lst), key=lst.count)

print(fun_most_frequent_element([1, 2, 2, 3, 3, 3, 4]))
