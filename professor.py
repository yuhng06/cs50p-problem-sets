import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        tries = 0
        while tries <3:
            try:
                guess = int(input(f'{x} + {y} = '))
                if guess == z :
                    score += 1
                    break
                else:
                    tries += 1
                    print('EEE')
            except ValueError:
                print('EEE')
                tries+=1
            except EOFError:
                break
        else:
            print(f'{x} + {y} = {z}')

    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level < 1 or level > 3:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
