# 合并两个字典
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def main():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = merge_dictionaries(dict1, dict2)
    print(f"Merged dictionary: {merged_dict}")

if __name__ == "__main__":
    main()
