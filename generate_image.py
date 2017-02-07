from matplotlib import pyplot as plt
import numpy as np
import PIL

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
x, y = np.meshgrid(x, y)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.contour(x, y, (y**2 - 4*x), [0])

canvas = plt.get_current_fig_manager().canvas
canvas.draw()
pil_image = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
