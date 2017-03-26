from gradient_descent import get_data

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
            print(' 6    Jupiter full (every 60 days since 2005 = one Jupiter year)')
            print(' 7    Halley full (every 30 days 1984 - 1987)')
            print(' 8    custom file path')

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
                data = get_data('data/jupiter.csv')
            elif answer == 7:
                data = get_data('data/halley.csv')
            elif answer == 8:
                data = get_data(input('Path: '))
            else:
                continue

            print('\nSelect start parameters:')
            print(' 1   default [10, 0, 10, 0, 0, 0]')
            print(' 2   Mars approximation [-100, 0, -100, -300, 200, 30000]')
            print(' 3   Mars half year wrong minimum (hyperbola) [-1017000, 39000, -299600, -2983000, 561000, 23157000]')
            print(' 4   Jupiter approximation [-813700, -6200, -785600, -6000, -1600, 5376000]')
            print(' 5   Saturn approximation [5541730, 107633, 6468945, 1673, -90184, 72001305]')
            print(' 6   Halley approximation [-1000, -1400, -600, -25000, 30000, 230000]')
            print(' 7   custom params')

            try: 
                answer = int(input('Your selection: '))
            except ValueError:
                params = [10, 0, 10, 0, 0, -300]
            if answer == 1:
                params = [10, 0, 10, 0, 0, -300]
            elif answer == 2:
                params = [-100, 0, -100, -300, 200, 30000]
            elif answer == 3:
                params = [-1017000, 39000, -299600, -2983000, 561000, 23157000]
            elif answer == 4:
                params = [-813700, -6200, -785600, -6000, -1600, 5376000]
            elif answer == 5:
                params = [5541730, 107633, 6468945, 1673, -90184, 72001305]
            elif answer == 6:
                params = [-1000, -1400, -600, -25000, 30000, 230000]
            elif answer == 7:
                params = [float(i) for i in input('Params separated by ,: ').split(',')]
            else:
                continue

            print('\nRecommended steps:')
            print(' Mars: 1e-7')
            print(' Earth: 1e-6')
            print(' Saturn: 7e-11')
            print(' Jupiter, Halley: 1e-9')

            try:
                step = float(input('Define step (default is 1e-6): '))
            except ValueError:
                step = 1e-6

            # load Earth data
            earth_data = get_data('data/earth.csv')

            done = True
        except ValueError:
            print('Invalid input!')
            print()
    return data, earth_data, params, step
