import math
lower = int(input('Enter A number for Lower Bond: '))
upper = int(input('Enter A number for Upper Bond: '))


def computer_guess():
    global upper, lower
    a = round(math.log(upper - lower + 1, 2))   # chance
    f = ''  # feedback
    while f != 'q':
        if lower != upper:
            guess = round((upper + lower - 1)/2)
        else:
            guess = lower   # or upper
        f = input(f'Is {guess} is High (h), Low (l) or correct(c): ').lower()     # feedback
        if f == 'h':
            upper = round((guess + lower)/2)
            a -= 1
        elif f == 'l':
            lower = round((guess + upper)/2)
            a -= 1
        elif f == 'c':
            print('yay Computer won')
            break
        if a == 0:
            print('Game Over')
            break


computer_guess()
