import random
import sys

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level < 1:
                raise ValueError
            break
        except ValueError:
            pass

    while True:
        try:
            guess = int(input('Guess: '))
            if guess < 1:
                raise ValueError
            else:
                predict = random.randint(1,level)
                if guess > predict:
                    print('Too large!')
                elif guess < predict:
                    print ('Too small!')
                else:
                    sys.exit('Just right!')
        except ValueError:
            pass

main()




