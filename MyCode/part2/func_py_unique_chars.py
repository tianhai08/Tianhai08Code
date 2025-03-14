# func_py_unique_chars.py

def func_py_unique_chars(text):
    return len(set(text)) == len(text)

def test_unique_chars():
    words = ["abcdef", "hello", "python", "123456"]
    for word in words:
        print(f"'{word}' has all unique characters: {func_py_unique_chars(word)}")

if __name__ == "__main__":
    test_unique_chars()
