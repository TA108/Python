a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))
c = int(input('Enter 3rd number:'))
if a > b and a > c:
    print('Number 1 is the greatest')
if b > a and b > c:
    print('Number 2 is the greatest')
if c > b and c > a:
    print('Number 3 is the greatest')