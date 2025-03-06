# func_py_check_password_strength.py
import re

def func_py_check_password_strength(password):
    if (len(password) >= 8 and re.search(r'[A-Z]', password) and 
        re.search(r'[a-z]', password) and re.search(r'\d', password) and 
        re.search(r'[@$!%*?&]', password)):
        return "Strong"
    return "Weak"

print(func_py_check_password_strength("P@ssw0rd"))
