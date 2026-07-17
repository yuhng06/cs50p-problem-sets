def main():
    total = 0.0
    while True:
        try:
            y = input('Item: ').title().strip()
            price = get_price(y)
            if price is not None:
                total = total + price
                print(f'Total: ${total:.2f}')
        except EOFError:
            break
        except ValueError:
            pass

def get_price(x):
    match x:
        case 'Baja Taco':
            return 4.25
        case 'Burrito':
            return 7.50
        case 'Bowl':
            return 8.50
        case 'Nachos':
            return 11.00
        case 'Quesadilla':
            return 8.50
        case 'Super Burrito':
            return 8.50
        case 'Super Quesadilla':
            return 9.50
        case 'Taco':
            return 3.00
        case 'Tortilla Salad':
            return 8.00
        case _:
            return None

main()
