#!/usr/local/bin/python3.7
# jHiggins = {
#     'firstName': 'joe',
#     'lastName': 'higgins',
#     'birthday': 'may 9',
#     'city': 'stockholm',
# }
# aMamalakis = {
#     'firstName': 'alex',
#     'lastName': 'mamalakis',
#     'birthday': 'may 16',
#     'city': 'houston',
# }
# cRawls = {
#     'firstName': 'camron',
#     'lastName': 'rawls',
#     'birthday': 'march 17',
#     'city': 'hick town',
# }
# people = [jHiggins, aMamalakis, cRawls]
#
# for userInfo in people:
#     print(userInfo['firstName'].title(),
#           userInfo['lastName'].title(), "is from",
#           userInfo['city'].title() +
#           ". His birthday is",
#           userInfo['birthday'].title())

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)