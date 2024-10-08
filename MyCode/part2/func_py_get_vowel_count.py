# func_py_get_vowel_count.py
def func_py_get_vowel_count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
