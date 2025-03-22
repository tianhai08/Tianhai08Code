# fun_py_check_anagram.py

def fun_py_check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def test_check_anagram():
    print(f"Are 'listen' and 'silent' anagrams? {fun_py_check_anagram('listen', 'silent')}")

if __name__ == "__main__":
    test_check_anagram()
