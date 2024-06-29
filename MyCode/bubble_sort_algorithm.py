# bubble_sort_algorithm.py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted array: {arr}")
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")
