from data import convert_line

def get_data(filename='data/mars.csv'):
    with open(filename, 'r') as F:
        text_data = F.readlines()

    data = []
    for line in text_data:
        data.append(convert_line(line))
    return data

def calculate_gradient(points, params, step):
    grad = [0 for i in range(6)]
    a, b, c, d, e, f = params
    for point in points:
        x, y = point
        part_result = a*x**2 + b*x*y + c*y**2 + d*x + e*y + f

        grad[0] += part_result * x**2 * step
        grad[1] += part_result * x*y * step
        grad[2] += part_result * y**2 * step
        grad[3] += part_result * x * step
        grad[4] += part_result * y * step
        grad[5] += part_result * step

    return grad
