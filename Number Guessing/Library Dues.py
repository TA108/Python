a = input('Are you a member? Y or N ?')
b = int(input('Days you have taken the book:'))
if a == "Y":
    if b < 30:
        print('You have no dues')
    elif b > 30:
        b -= 30
        print('you are late by', b)
        b *= 2
        print('You have', b, 'fine')

else:
    Print("You are not a member")