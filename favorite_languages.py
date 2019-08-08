#!/usr/local/bin/python3.7

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah', 'john', 'rick']
people = ['phil', 'pooky', 'pokpok', 'pwet', 'dede', 'sarah']
favpeeps = list(favorite_languages.keys())
allpeeps = favpeeps + people + friends

#print(set(allpeeps),'\n')
#print(favpeeps)

take = ', will you take our poll?'
thanks = ', thanks for taking the poll.'
buddy = 'My best buddy, '
fav = '\tYour favorite language is: '

for person in set(allpeeps):
    if person in favorite_languages.keys():
        if person in friends:
            print(buddy + person.title() + thanks)
            print(fav + favorite_languages[person].title())
        else:
            print(person.title() + thanks)
            print(fav + favorite_languages[person].title())
    elif person not in favorite_languages.keys():
        if person in friends:
            print(buddy + person.title() + take)
        else:
            print(person.title() + take)


#print("\n")

#print("Sarah's favorite language is " +
#    favorite_languages['sarah'].title() +
#    ".")

#print("\n")

#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " +
#        language.title() + ".")

#print("\n")

#for name in favorite_languages.keys():
#    print(name.title())

#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")

#print("\n")

#for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking the poll.")

print("\n")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


