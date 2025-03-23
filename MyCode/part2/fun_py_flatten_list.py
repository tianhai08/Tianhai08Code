# fun_py_flatten_list.py

def fun_py_flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def test_flatten_list():
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"Flattened list: {fun_py_flatten_list(nested)}")

if __name__ == "__main__":
    test_flatten_list()
