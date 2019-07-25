#!/usr/local/bin/python3.7

person = {
    'first_name': 'joe',
    'last_name': 'higgins',
    'age': '29',
    'city': 'stockholm',
    }

for key in person:
    if key == 'first_name':
        print("Meet " + person[key].title())
    if key == 'last_name':
        print("He's a member of the " + person[key].title() + " clan.")
    if key == 'age':
        print("He's " + person[key] + " years old")
    if key == 'city':
        print("He lives in " + person[key].title())

