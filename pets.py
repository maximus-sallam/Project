riley = {
    'animalKind': 'dog',
    'ownerName': 'ven',
    'age': '3',
}

bucky = {
    'animalKind': 'demon',
    'ownerName': 'venice',
    'age': '1',
}

alden = {
    'animalKind': 'prisoner',
    'ownerName': 'chito',
    'age': '4',
}

pets = [alden, bucky, riley]

for pet in pets:
    for key, value in pet.items():
        print(key.title(), value.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)