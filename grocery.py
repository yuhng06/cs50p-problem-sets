def main():
    groceries = {}

    while True:
        try:
            item = input().strip().lower()
            if item in groceries:
                groceries[item]+=1
            else:
                groceries[item]=1
        except EOFError:
            break
        except ValueError:
            pass

    for item in sorted(groceries):
        print(f'{groceries[item]} {item.upper()}')

main()
