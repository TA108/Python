import random


def play():
    a = input('(R) for rock, (P) for paper and (S) for Scissors: ').lower()
    b = random.choice(['r', 'p', 's'])
    print(b)
    if a == b:
        print('it\'s a tie')

    if win(a, b):
        print('You Won')

    if win(b, a):
        print('You lost')


def win(player_1, player_2):
    if ((player_1 == 'r' and player_2 == 's') or (player_1 == 'p' and player_2 == 'r') or
            (player_1 == 's' and player_2 == 'p')):
        return True


play()
