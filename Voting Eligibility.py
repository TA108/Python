name = input('Enter name:')
age = int(input('Enter age:'))

if age >= 18:
    print(name, "you can vote as you are of age", age)
else:
    print(name, "you can't vote as you are of age", age)