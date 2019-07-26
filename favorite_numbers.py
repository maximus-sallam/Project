#!/usr/local/bin/python3.7

numbers = {
    'joe': '9',
    'alex': '6',
    'max': '69',
    'ven': '7',
    'cortney': '8',
    }

fav = '\'s favorite number is '

for key in numbers:
    if key == 'joe':
        print(key.title() + fav + str(numbers[key]))
    if key == 'alex':
        print(key.title() + fav + numbers[key])
    if key == 'max':
        print(key.title() + fav + numbers[key] + ". lol")
    if key == 'ven':
        print(key.title() + fav + numbers[key])
    if key == 'cortney':
        print(key.title() + fav + numbers[key])

