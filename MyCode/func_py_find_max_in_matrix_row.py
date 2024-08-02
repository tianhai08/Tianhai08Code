# func_py_find_max_in_matrix_row.py
def func_py_find_max_in_matrix_row(matrix, row_index):
    return max(matrix[row_index])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(func_py_find_max_in_matrix_row(matrix, 1))
