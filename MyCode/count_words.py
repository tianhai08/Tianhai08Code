# count_words.py
def count_words(s):
    words = s.split()
    return len(words)

if __name__ == "__main__":
    s = input("Enter a string: ")
    word_count = count_words(s)
    print(f"The number of words in the string is: {word_count}")
