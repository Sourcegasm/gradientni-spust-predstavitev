import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
import time

data = [[-1.3669, 5.06791], [-1.51623, 5.10966], [-1.66176, 5.13864], [-1.80315, 5.15478], [-1.94002, 5.15803],
[-2.07205, 5.14838], [-2.1989, 5.12587], [-2.32025, 5.09055], [-2.43581, 5.0425], [-2.54527, 4.98185],
[-2.64837, 4.90875], [-2.74486, 4.82338], [-2.83448, 4.72595], [-2.91702, 4.61671], [-2.99227, 4.49594],
[-3.06003, 4.36392], [-3.12015, 4.22099]]

def grad_part(x, y, params):
    return params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]

def grad_a(points, params, step):
    s = 0.0
    for point in points:
        s += step * grad_part(point[0], point[1], params)*point[0]**2
    return s

def grad_b(points, params, step):
    s = 0.0
    for point in points:
        s += step * grad_part(point[0], point[1], params)*point[0]*point[1]
    return s

def grad_c(points, params, step):
    s = 0.0
    for point in points:
        s += step * grad_part(point[0], point[1], params)*point[1]**2
    return s

def grad_d(points, params, step):
    s = 0.0
    for point in points:
        s += step * grad_part(point[0], point[1], params)*point[0]
    return s

def grad_e(points, params, step):
    s = 0.0
    for point in points:
        s += step * grad_part(point[0], point[1], params)*point[1]
    return s

def grad_f(points, params, step):
    s = 0.0
    for point in points:
        s += step * grad_part(point[0], point[1], params)
    return s

# params = [0.8, 0.4, 0.4, 1, -1.4, -1]
params = [1, 0, 0.1, 0.5, -1, -0.5]
step = 1e-4

if __name__ == '__main__':
    window = tk.Frame()
    window.master.title("Gradientni spust")

    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)
    x, y = np.meshgrid(x, y)
    fig = Figure(figsize=(8, 8), dpi=100)

    ax1 = fig.add_subplot(111)

    points_x = [j[0] for j in data]
    points_y = [j[1] for j in data]

    ax2 = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=window.master)
    canvas.show()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2TkAgg(canvas, window.master)
    toolbar.update()
    canvas._tkcanvas.pack()

    for i in range(200):
        new_params = params[:]
        new_params[0] -= grad_a(data, params, step)
        new_params[1] -= grad_b(data, params, step)
        new_params[2] -= grad_c(data, params, step)
        new_params[3] -= grad_d(data, params, step)
        new_params[4] -= grad_e(data, params, step)
        new_params[5] -= grad_f(data, params, step)
        params = new_params[:]

        ax1.contour(x, y, (params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]), [0])
        ax2.scatter(points_x, points_y)
        canvas.draw()
        ax1.clear()

        window.update()
    ax1.contour(x, y, (params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]), [0])
    ax2.scatter(points_x, points_y)
    canvas.draw()

    string = '{0}*x^2{1:+}*x*y{2:+}*y^2{3:+}*x{4:+}*y{5:+} = 0'.format(*params)
    string = string.replace('+', ' + ').replace('-', ' - ')
    print(string)

    window.mainloop()
