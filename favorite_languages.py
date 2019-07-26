#!/usr/local/bin/python3.7

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

print("\n")

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

print("\n")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

for name in favorite_languages.keys():
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
