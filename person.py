#!/usr/local/bin/python3.7
jHiggins = {
    'firstName': 'joe',
    'lastName': 'higgins',
    'birthday': 'may 9',
    'city': 'stockholm',
}
aMamalakis = {
    'firstName': 'alex',
    'lastName': 'mamalakis',
    'birthday': 'may 16',
    'city': 'houston',
}
cRawls = {
    'firstName': 'camron',
    'lastName': 'rawls',
    'birthday': 'march 17',
    'city': 'hick town',
}
people = [jHiggins, aMamalakis, cRawls]

for userInfo in people:
    print(userInfo['firstName'].title(),
          userInfo['lastName'].title(), "is from",
          userInfo['city'].title() +
          ". His birthday is",
          userInfo['birthday'].title())
