# func_py_file_line_count.py
def func_py_file_line_count(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

print(func_py_file_line_count("example.txt"))
