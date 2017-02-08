import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk

from gradient_decent import calculate_gradient, get_data

data = get_data()
data = data[:20]

# params = [10, 0, 10, 0, 0, 0]
params = [10, 0, 10, 0, 0, -300]
step = 1e-6

if __name__ == '__main__':
    window = tk.Frame()
    window.master.title("Gradientni spust")

    x = np.linspace(-17, 15, 1000)
    y = np.linspace(-15, 17, 1000)
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
        gradient = calculate_gradient(data, params, step)
        for j in range(len(params)):
            params[j] -= gradient[j]

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
