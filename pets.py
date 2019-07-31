# riley = {
#     'animalKind': 'dog',
#     'ownerName': 'ven',
#     'age': '3',
# }

# bucky = {
#     'animalKind': 'demon',
#     'ownerName': 'venice',
#     'age': '1',
# }

# alden = {
#     'animalKind': 'prisoner',
#     'ownerName': 'chito',
#     'age': '4',
# }

# pets = [alden, bucky, riley]

# for pet in pets:
#     for key, value in pet.items():
#         print(key.title(), value.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

def describe_pet(animal_type='pussy', pet_name='delicious'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'riley')
describe_pet(pet_name='dick', animal_type='penis')
describe_pet()
describe_pet(pet_name='yummy')