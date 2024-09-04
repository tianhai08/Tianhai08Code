# func_py_generate_gray_code.py
def func_py_generate_gray_code(n):
    if n == 0:
        return ["0"]
    if n == 1:
        return ["0", "1"]
    prev = func_py_generate_gray_code(n - 1)
    return ["0" + code for code in prev] + ["1" + code for code in reversed(prev)]

print(func_py_generate_gray_code(3))
