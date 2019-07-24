#!/usr/local/bin/python3.7

age = int(input("How many years since the person was born? "))

if (age < 0):
    person = 'not born yet'
elif (age < 2):
    person = 'baby'
elif (age < 4):
    person = 'toddler'
elif (age < 13):
    person = 'kid'
elif (age < 20):
    person = 'teenager'
elif (age < 65):
    person = 'adult'
elif (age < 120):
    person = 'elder'
elif (age >=120):
    person = 'dead'
else:
    person = 'imaginary'

this_one = 'This person is '
this_two = 'This person is a '
this_thr = 'This person is an '

if (person == 'imaginary'):
    print(this_one + person + "!")

if (person == 'dead'):
    print(this_one + person + "!")
elif (person == 'elder'):
    print(this_thr + person + "!")
elif (person == 'adult'):
    print(this_thr + person + "!")
elif (person == 'teenager'):
    print(this_two + person + "!")
elif (person == 'kid'):
    print(this_two + person + "!")
elif (person == 'toddler'):
    print(this_two + person + "!")
elif (person == 'baby'):
    print(this_two + person + "!")
elif (person == 'not born yet'):
    print(this_one + person + "!")
else:
    print("I don't know what to tell you")

