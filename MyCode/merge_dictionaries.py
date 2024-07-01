# merge_dictionaries.py
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = merge_dicts(dict1, dict2)
    print(f"Merged dictionary: {merged_dict}")
