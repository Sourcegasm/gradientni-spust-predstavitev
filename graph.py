import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk

from gradient_decent import calculate_gradient, get_data

def select_data():
    done = False
    while not done:
        try:
            print('Select input data set:')
            print(' 1    Mars half year')
            print(' 2    Mars full (whole year measured every Earth month)')
            print(' 3    Mars small (every fourth point of \'Mars full\')')
            print(' 4    Earth full (every 14 days)')
            print(' 5    Saturn full (every 100 days since 1987 = one Saturn year)')
            print(' 6    Halley full (every 30 days 1984 - 1987)')
            print(' 7    custom file path')

            answer = int(input('Your selection: '))

            if answer == 1:
                data = get_data('data/mars_half_year.csv')
            elif answer == 2:
                data = get_data('data/mars_full.csv')
            elif answer == 3:
                data = get_data('data/mars_full.csv')[::4]
            elif answer == 4:
                data = get_data('data/earth.csv')
            elif answer == 5:
                data = get_data('data/saturn.csv')
            elif answer == 6:
                data = get_data('data/halley.csv')
            elif answer == 7:
                data = get_data(input('Path: '))
            else:
                continue

            print()
            print('Select start parameters:')
            print(' 1   default [10, 0, 10, 0, 0, 0]')
            print(' 2   Mars approximation [-100, 0, -100, -300, 200, 30000]')
            print(' 3   Saturn approximation [-5000, 0, -5000, 2000, -70000, 72000000]')
            print(' 4   Halley approximation [-1000, -1400, -600, -25000, 30000, 230000]')
            print(' 5   custom params')

            answer = int(input('Your selection: '))
            if answer == 1:
                params = [10, 0, 10, 0, 0, -300]
            elif answer == 2:
                params = [-100, 0, -100, -300, 200, 30000]
            elif answer == 3:
                params = [-5000, 0, -5000, 2000, -70000, 72000000]
            elif answer == 4:
                params = [-1000, -1400, -600, -25000, 30000, 230000]
            elif answer == 5:
                params = [int(i) for i in input('Params separated by ,: ').split(',')]
            else:
                continue

            print()
            print('Recommended steps:')
            print(' Mars: 1e-7')
            print(' Earth: 1e-6')
            print(' Saturn: 1e-10')
            print(' Halley: 1e-9')

            try:
                step = float(input('Define step (default is 1e-6): '))
            except:
                step = 1e-6

            # load Earth data
            earth_data = get_data('data/earth.csv')

            done = True
        except ValueError:
            print('Invalid input!')
            print()
    return data, earth_data, params, step


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

    for i in range(200):
        gradient = calculate_gradient(data, params, step)
        if sum((abs(i) for i in gradient)) <= 1e-3:
            print(i, 'steps')
            break
        for j in range(len(params)):
            params[j] -= gradient[j]

        ax1.contour(x, y, (params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]), [0])
        ax2.scatter(points_x, points_y, color='k')
        ax2.scatter(0, 0, color='y')
        ax2.scatter(earth_points_x, earth_points_y)
        canvas.draw()
        ax1.clear()

        window.update()

    ax1.contour(x, y, (params[0]*x**2 + params[1]*x*y + params[2]*y**2 + params[3]*x + params[4]*y + params[5]), [0])
    ax2.scatter(points_x, points_y, color='k')
    ax2.scatter(0, 0, color='y')
    ax2.scatter(earth_points_x, earth_points_y)
    canvas.draw()

    string = '{0}*x^2{1:+}*x*y{2:+}*y^2{3:+}*x{4:+}*y{5:+} = 0'.format(*params)
    string = string.replace('+', ' + ').replace('-', ' - ')
    print()
    print('Result:')
    print(string)

    window.mainloop()
