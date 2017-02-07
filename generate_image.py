from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import time

data_set = [[1, 1], [2, 2], [1, 3], [-1, -6]]

def get_image(i=0):
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    x, y = np.meshgrid(x, y)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.contour(x, y, (y**2 - 4*x + i), [0])

    points_x = [j[0] for j in data_set]
    points_y = [j[1] for j in data_set]
    ax2 = fig.add_subplot(111)
    ax2.scatter(points_x, points_y)

    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    plt.close('all')

    pil_image = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    return pil_image



if __name__ == '__main__':
    window = tk.Frame()
    window.master.title("Gradientni spust")

    image = get_image()
    tk_image = ImageTk.PhotoImage(image)

    image_label = tk.Label(image=tk_image)
    image_label.image = tk_image
    image_label.pack()

    for i in range(100):
        tk_image = ImageTk.PhotoImage(get_image(i))
        image_label.configure(image=tk_image)
        image_label.image = tk_image
        window.update()

    window.mainloop()
