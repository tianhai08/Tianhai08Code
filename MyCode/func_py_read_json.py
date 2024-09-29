# func_py_read_json.py
import json

def func_py_read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# 示例用法
print(func_py_read_json("data.json"))
