a = [1, 3, -4, 5, -6, 7, -434, 43]
odd, even, neg, pos = 0, 0, 0, 0
for i in a:
    if i % 2 == 0:
        even += 1
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1
    if i % 2 != 0:
        odd += 1

print('Number of odd\'s are', odd, 'and even are', even,
      '\nPositive', pos, 'and Negative', neg)
