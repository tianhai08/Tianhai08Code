# fun_get_file_size.py
import os

def fun_get_file_size(filename):
    return os.path.getsize(filename)

print(fun_get_file_size('example.txt'))
