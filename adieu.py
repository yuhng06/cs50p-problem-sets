import inflect

def main():
    p = inflect.engine()

    names = []

    try:
        while True:
            name = input('Name: \n').title()
            names.append(name)

    except EOFError:
        print(f'Adieu, adieu, to {p.join(names)}')

main()
