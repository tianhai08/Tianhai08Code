# func_py_text_summary.py
from collections import Counter
import re

def func_py_text_summary(text):
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(5)

print(func_py_text_summary("This is a test. This is only a test."))
