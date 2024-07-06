# fun_folder_size.py
import os

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            total_size += os.path.getsize(file_path)
    return total_size

path = "."
print(f"Total size of '{path}' folder: {get_folder_size(path)} bytes")
