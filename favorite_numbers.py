#!/usr/local/bin/python3.7

numbers = {
    'joe': ['9', '18', '27'],
    'alex': ['6','66', '666'],
    'max': ['69', '42', '64'],
    'ven': ['7', '21', '5'],
    'cortney': ['8', '4', '2'],
    }

fav = '\'s favorite number is'

for key, value in numbers.items():
    if key == 'joe':
        print(key.title() + fav, ", ".join(numbers[key]))
    if key == 'alex':
        print(key.title() + fav, ", ".join(numbers[key]))
    if key == 'max':
        print(key.title() + fav, ", ".join(numbers[key]) + ". lol")
    if key == 'ven':
        print(key.title() + fav, ", ".join(numbers[key]))
    if key == 'cortney':
        print(key.title() + fav, ", ".join(numbers[key]))

