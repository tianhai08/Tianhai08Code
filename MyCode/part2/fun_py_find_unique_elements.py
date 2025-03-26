# fun_py_find_unique_elements.py

def fun_py_find_unique_elements(lst):
    return list(set(lst))

def test_find_unique_elements():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"Unique elements: {fun_py_find_unique_elements(numbers)}")

if __name__ == "__main__":
    test_find_unique_elements()
