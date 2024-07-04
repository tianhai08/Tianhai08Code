# max_min_in_list.py
def find_max_min(lst):
    return max(lst), min(lst)

if __name__ == "__main__":
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    maximum, minimum = find_max_min(lst)
    print(f"The maximum value is: {maximum}")
    print(f"The minimum value is: {minimum}")
