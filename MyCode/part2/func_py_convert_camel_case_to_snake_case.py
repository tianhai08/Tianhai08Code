# func_py_convert_camel_case_to_snake_case.py
import re

def func_py_convert_camel_case_to_snake_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()
