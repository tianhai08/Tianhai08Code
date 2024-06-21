# is_alpha_string.py
def is_alpha_string(s):
    return s.isalpha()

string1 = "HelloWorld"
string2 = "Hello World123"
print(f"Is '{string1}' all alphabetic? {is_alpha_string(string1)}")
print(f"Is '{string2}' all alphabetic? {is_alpha_string(string2)}")
