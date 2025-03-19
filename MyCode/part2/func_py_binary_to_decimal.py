# func_py_binary_to_decimal.py

def func_py_binary_to_decimal(binary):
    return int(binary, 2)

def test_binary_to_decimal():
    print(func_py_binary_to_decimal("1010"))

if __name__ == "__main__":
    test_binary_to_decimal()
