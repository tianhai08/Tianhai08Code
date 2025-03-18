# func_py_common_elements.py

def func_py_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def test_common_elements():
    list1 = [10, 20, 30, 40]
    list2 = [30, 40, 50, 60]
    print(f"Common elements: {func_py_common_elements(list1, list2)}")

if __name__ == "__main__":
    test_common_elements()
