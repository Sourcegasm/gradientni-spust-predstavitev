import numpy as np

def load_data():
    with open('data/houses.cvs') as F:
        data = F.readlines()

    # data format: price, house area, land area, construction year, renovation year
    A, b = [], []

    for i in range(len(data)):
        price, house_area, area, con_year, ren_year = [float(i) for i in data[i].split(',')]
        b.append(price / 1000)
        A.append([house_area, area, 2017 - con_year, 2017 - ren_year, 1])

    A = np.array(A)
    b = np.array(b)

    return A, b

def predict_price(house, x):
    price = 0
    for i in range(len(x)):
        price += house[i] * x[i]
    return int(price) * 1000


if __name__ == '__main__':
    A, b = load_data()
    x = np.linalg.lstsq(A, b)[0]
    print(x)

    while True:
        house_area = float(input('Kvadratura: '))
        area = float(input('Zemljišče: '))
        con_year = 2017 - int(input('Leto gradnje: '))
        try:
            ren_year = 2017 - int(input('Leto obnove: '))
        except ValueError:
            ren_year = con_year

        house = house_area, area, con_year, ren_year, 1
        print('Predvidena cena: {:,}€\n'.format(predict_price(house, x)))
