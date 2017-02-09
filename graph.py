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
            print(' 6    custom file path')

            answer = int(input('Your selection: '))
            
            if answer == 1: data = get_data('data/mars_half_year.csv')
            elif answer == 2: data = get_data('data/mars_full.csv')
            elif answer == 3: data = get_data('data/mars_full.csv')[::4]
            elif answer == 4: data = get_data('data/earth.csv')
            elif answer == 5: data = get_data('data/saturn.csv')
            elif answer == 6: data = get_data(input('Path: '))
            else: continue

            params_list = [[10, 0, 10, 0, 0, -300], [-100, 0, -100, -300, 200, 30000]]

            print('\nSelect start parameters:')
            print(' 1   default', params_list[0])
            print(' 2   Mars approximation', params_list[1])
            print(' 3   custom params')

            try:
                answer = int(input('Your selection: '))
            except:
                answer = 1
            if answer == 1: params = params_list[0]
            elif answer == 2: params = params_list[1]
            elif answer == 3: params = [float(i) for i in input('Params separated by ,: ').split(',')]
            else: continue

            print()
            try:
                step = float(input('Define step (default is 1e-6): '))
            except:
                step = 1e-6
            done = True
        except ValueError:
            print('Invalid input!\n')
            
    return data, params, step


if __name__ == '__main__':
    data, params, step = select_data()
    print('Procesing...')
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
    print()
    print('Result:')
    print(string)

    window.mainloop()
