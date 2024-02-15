import random

a = random.randint(1, 100)

print('The number computer has to guess is:', a)

chance = 100

lower_bound = 1
upper_bound = 100

while True:
    guess = (lower_bound + upper_bound) // 2
    if a < guess:
        upper_bound = guess - 1
        chance -= 1
        print('guess:', guess, '\n', 'Chance:', chance)

    elif a > guess:
        lower_bound = guess + 1
        chance -= 1
        print('guess:', guess, '\n', 'Chance:', chance)

    elif a == guess:
        print('Computer won')
        break

    if chance == 0:
        print('Game Over')
        break
