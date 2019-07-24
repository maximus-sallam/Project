#!/usr/local/bin/python3.7
alien_color = 'red'

if (alien_color == 'green'):
    print("Player has earned 5 points!")
else:
    print("Player has earned 10 points!")


if (alien_color == 'red'):
    point = 5
else:
    point = 10

print("Player has earned " + str(point) + " points!")

