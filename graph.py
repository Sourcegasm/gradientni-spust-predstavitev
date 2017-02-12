import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
import time

from gradient_decent import calculate_gradient
from select_data import select_data

# set to True to speed up animations
DEBUG = False

if __name__ == '__main__':
    data, earth_data, params, step = select_data()
    print('Procesing...')

    window = tk.Frame()
    window.master.title("Gradientni spust")

    # separate points to x and y arrays
    points_x = [j[0] for j in data]
    points_y = [j[1] for j in data]
    earth_points_x = [j[0] for j in earth_data]
    earth_points_y = [j[1] for j in earth_data]

    max_x = max(points_x)
    min_x = min(points_x)
    max_y = max(points_y)
    min_y = min(points_y)

    x = np.linspace(min(min_x, min_y)-10, max(max_x, max_y)+10, 1000)
    y = np.linspace(min(min_x, min_y)-10, max(max_x, max_y)+10, 1000)
    x, y = np.meshgrid(x, y)
    fig = Figure(figsize=(8, 8), dpi=100)

    ax1 = fig.add_subplot(111)

    ax2 = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=window.master)
    canvas.show()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2TkAgg(canvas, window.master)
    toolbar.update()
    canvas._tkcanvas.pack()

    N = 100
    for i in range(N):
        print('\rProgress: [' + '#' * int(i / N * 20) + ' ' * (20 - int(i / N * 20)) + ']', end=' ')
        gradient = calculate_gradient(data, params, step)

        error = sum((abs(i) for i in gradient))
        if error <= len(data) * 1e-4:
            print('\n', i, 'steps')
            break

        for j in range(len(params)):
            params[j] -= gradient[j]

        ax1.contour(x, y, (params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]), [0])
        ax2.scatter(points_x, points_y, color='k')
        ax2.scatter(0, 0, color='y')
        ax2.scatter(earth_points_x, earth_points_y)
        canvas.draw()
        ax1.clear()

        if not DEBUG:
            time.sleep(0.1)

        window.update()

    print('\r')

    ax1.contour(x, y, (params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]), [0])
    ax2.scatter(points_x, points_y, color='k')
    ax2.scatter(0, 0, color='y')
    ax2.scatter(earth_points_x, earth_points_y)
    canvas.draw()

    string = '{0}*x^2{1:+}*x*y{2:+}*y^2{3:+}*x{4:+}*y{5:+} = 0'.format(*params)
    string = string.replace('+', ' + ').replace('-', ' - ')
    
    print('\nResult:')
    print(string)

    window.mainloop()
