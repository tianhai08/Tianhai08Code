# func_py_generate_fibonacci_series.py
def func_py_generate_fibonacci_series(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

print(func_py_generate_fibonacci_series(10))
