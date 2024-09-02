# func_py_calculate_eight_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_eight_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.sin(t)
    y = a * np.sin(t) * np.cos(t)
    plt.plot(x, y)
    plt.title("Eight Curve")
    plt.show()

func_py_calculate_eight_curve(5, 1000)
