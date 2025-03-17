# func_py_gcd.py

import math

def func_py_gcd(a, b):
    return math.gcd(a, b)

def test_gcd():
    pairs = [(48, 18), (101, 103), (56, 98)]
    for a, b in pairs:
        print(f"GCD of {a} and {b}: {func_py_gcd(a, b)}")

if __name__ == "__main__":
    test_gcd()
