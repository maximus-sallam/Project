#!/usr/local/bin/python3.7

jHiggins = {
    'first_name': 'joe',
    'last_name': 'higgins',
    'birthday': 'may 9',
    'city': 'stockholm',
}

aMamalakis = {
    'first_name': 'alex',
    'last_name': 'mamalakis',
    'birthday': 'may 16',
    'city': 'houston',
}

cRawls = {
    'first_name': 'camron',
    'last_name': 'rawls',
    'birthday': 'march 17',
    'city': 'hick town',
}

people = [jHiggins, aMamalakis, cRawls]

for userInfo in people:
    print(userInfo['first_name'].title(),
          userInfo['last_name'].title(), "is from ",
          userInfo['city'].title() +
          ". His birthday is",
          userInfo['birthday'].title())
