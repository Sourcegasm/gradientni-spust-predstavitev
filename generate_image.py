import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
import time

data_set = [[1, 1], [2, 2], [1, 3], [-1, -6]]

if __name__ == '__main__':
    window = tk.Frame()
    window.master.title("Gradientni spust")

    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    x, y = np.meshgrid(x, y)
    fig = Figure(figsize=(8, 8), dpi=100)
    ax1 = fig.add_subplot(111)
    ax1.contour(x, y, (y**2 - 4*x), [0])

    points_x = [j[0] for j in data_set]
    points_y = [j[1] for j in data_set]
    ax2 = fig.add_subplot(111)
    ax2.scatter(points_x, points_y)

    canvas = FigureCanvasTkAgg(fig, master=window.master)
    canvas.show()
    canvas.get_tk_widget().pack()

    for i in range(100):
        ax1.contour(x, y, (y**2 - 4*x + i), [0])
        ax2.scatter(points_x, points_y)
        canvas.draw()
        ax1.clear()

        window.update()

    window.mainloop()
