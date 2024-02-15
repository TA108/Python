#name = input('Enter your name:')
#age =  int(input('enter age'))
eng = int(input('enter marks for eng:'))
maths = int(input('enter marks for maths:'))
sci = int(input('enter marks for science:'))

if eng >= 70 or maths >= 70 or sci >= 70 :
    print('You Have Passed')
    if 80 > eng > 70 or 80 > maths > 70 or 80 > sci > 70:
        print('Your grade is: C')
    elif 90 > eng > 80 or 90 > maths > 80 or 90> sci > 80:
        print('Your grade is: B')
    elif eng > 90 or maths > 90 or sci > 90:
        print('Your grade is: A')
    if eng == 100 or maths == 100 or sci == 100:
        print('Congo you got Full marks in all 3 subjects')
else:
    print("You failed")