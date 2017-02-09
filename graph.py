import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk

from gradient_decent import calculate_gradient, get_data

done = False

while not done:
    try:
        print('Select input data set:')
        print(' 1    Mars full (0.5 year)')
        print(' 2    Mars small (45 random coordinates)')
        print(' 3    Earth full (every 14 days)')
        print(' 4    Saturn full (every 100 days since 1987 - one Saturn year)')
        print(' 5    custom file path')

        answer = int(input('Your selection: '))
        
        if answer == 1: data = get_data('data/mars_full.csv')
        elif answer == 2:
            data = get_data('data/mars.csv')
            data = data[:25] + data[30:45]
        elif answer == 3: data = get_data('data/earth.csv')
        elif answer == 4: data = get_data('data/saturn.csv')
        elif answer == 5: data = get_data(input('Path: '))
        else: continue

        print()
        print('Select start parameters:')
        print(' 1   default [10, 0, 10, 0, 0, 0]')
        print(' 2   Mars approximation [-100, 0, -100, -300, 200, 30000]')
        print(' 3   custom params')

        answer = int(input('Your selection: '))
        if answer == 1: params = [10, 0, 10, 0, 0, -300]
        elif answer == 2: params = [-100, 0, -100, -300, 200, 30000]
        elif answer == 3: params = [int(i) for i in input('Params separated by ,: ').split()]
        else: continue

        print()
        try:
            step = float(input('Define step (default is 1e-6): '))
        except:
            step = 1e-6
        done = True
    except ValueError:
        print('Invalid input!')
        print()

print('Procesing...')

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
        if sum((abs(i) for i in gradient)) <= 1e-3:
            print(i, 'steps')
            break
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
