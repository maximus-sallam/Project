#!/usr/local/bin/python3.7

person = {
    'first_name': 'joe',
    'last_name': 'higgins',
    'birthday': 'may 9',
    'city': 'stockholm',
    }

for key in person:
    if key == 'first_name':
        print("Meet " + person[key].title())
    if key == 'last_name':
        print("He's a member of the " + person[key].title() + " clan.")
    if key == 'birthday':
        print("His birthday is on " + person[key] + "th.")
    if key == 'city':
        print("He lives in " + person[key].title())

