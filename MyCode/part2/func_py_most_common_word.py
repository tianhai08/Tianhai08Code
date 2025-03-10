# func_py_most_common_word.py
from collections import Counter
import re

def func_py_most_common_word(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(1)[0] if words else None

print(func_py_most_common_word("Hello world! Hello again."))
