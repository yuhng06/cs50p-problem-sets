def main():
    fuel_fract = get_int()
    gauge = conditions(fuel_fract)
    print(gauge)

def get_int():
    while True:
        try:
            amt = input('Fraction: ')
            x, y = amt.split('/')
            x = int(x)
            y = int(y)
            if y == 0 or y<0 or x>y or x<0:
                raise ValueError
            else:
                return round (100*x/y)
        except ValueError:
            pass

def conditions(fuel):
    if (fuel>98):
        return('F')
    elif (fuel<2):
        return('E')
    else:
        return f'{fuel}%'

main()
