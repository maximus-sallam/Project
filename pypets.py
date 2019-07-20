#!/usr/local/bin/python3.7
## Set available pet types and actions
petTypes = ('dog', 'cat', 'rabbit', 'lizard', 'bird', 'fish','unicorn')
petActions = ('feed', 'walk', 'play', 'sleep', 'nap','kill')

## Pet class
class Pet():
    """Pet class"""
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.heath = 100
        self.happy = 100
        self.rest = 100
        self.hunger = 0

    def get_health(self):
        return self.health

    def get_happy(self):
        return self.happy

    def get_rest(self):
        return self.rest

    def get_hunger(self):
        return self.hunger

    def update_health(self, health):
        self.health = health

    def update_happy(self, happy):
        self.happy = happy

    def update_rest(self, rest):
        self.rest = rest

    def update_hunger(self, hunger):
        self.hunger = hunger

    def feed(self):
        """Pet eats"""
        print(self.name + " eats what you gave them.")

    def walk(self):
        """Walk pet"""
        print("You take " + self.name + " for a walk.")

    def play(self):
        """Pet plays"""
        print("You play with" + self.name + ".")

    def sleep(self):
        """Pet sleeps"""
        print(self.name + " sleeps.")

    def nap(self):
        """Pet naps"""
        print(self.name + " takes a nap.")

    def kill(self):
        """Pet dies"""
        print("You murdered " + self.name + ". You monster!")

## End of pet class
## Species Classes
class Dog(Pet):
	"""Dog class"""

	def __init__(self, name, owner):
		"""Initialize attributes of the Pet class"""
		super().__init__(name, owner)


class Cat(Pet):
	"""Cat class"""

	def __init__(self, name, owner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(name, owner)

class Rabbit(Pet):
	"""Rabbit class"""

	def __init__(self, name, owner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(name, owner)

class Lizard(Pet):
	"""Lizard class"""

	def __init__(self, name, owner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(name, owner)

class Bird(Pet):
	"""Bird class"""

	def __init__(self, name, owner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(name, owner)

class Fish(Pet):
	"""Fish class"""

	def __init__(self, name, owner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(name, owner)

class Unicorn(Pet):
    """Unicorn class"""

    def __init__(self, name, owner):
        """Initialize attibutes of the Pet class"""
        super().__init__(name, owner)

##End of species classes

## Get player name
owner = input("Welcome to pypets! \nWhat is your name?\n\t").title()
print("what kind of pet would you like?\n\t")
typeMenuNumber = 1
for types in petTypes:
	print(str(typeMenuNumber) + " " + types)
	typeMenuNumber += 1

typeChoice = int(input("number: "))
petType = petTypes[typeChoice-1]

name = input("What would you like to name your " + petType +"?\n\t")

## Sorry, alpha
if typeChoice == 1:
	player_dog = Dog(name, owner)
	print("\n\nOk, " + player_dog.owner + " your new " + petType + " is named " + player_dog.name + "!")
	currentPet = player_dog
elif typeChoice == 2:
	player_cat = Cat(name, owner)
	print("\n\nOk, " + player_cat.owner + " your new " + petType + " is named " + player_cat.name + "!")
	currentPet = player_cat
elif typeChoice == 3:
	player_rabbit = Rabbit(name, owner)
	print("\n\nOk, " + player_rabbit.owner + " your new " + petType + " is named " + player_rabbit.name + "!")
	currentPet = player_rabbit
elif typeChoice == 4:
	player_lizard = Lizard(name, owner)
	print("\n\nOk, " + player_lizard.owner + " your new " + petType + " is named " + player_lizard.name + "!")
	currentPet = player_lizard
elif typeChoice == 5:
	player_bird = Bird(name, owner)
	print("\n\nOk, " + player_bird.owner + " your new " + petType + " is named " + player_bird.name + "!")
	currentPet = player_bird
elif typeChoice == 6:
	player_fish = Fish(name, owner)
	print("\n\nOk, " + player_fish.owner + " your new " + petType + " is named " + player_fish.name + "!")
	currentPet = player_fish
elif typeChoice == 7:
    player_unicorn = Unicorn(name, owner)
    print("\n\nOk, " + player_unicorn.owner + " your new " + petType + " is named" + player_unicorn.name + "!")
    currentPet = player_unicorn
else:
	print("Sorry, that isn't a valid option")
	exit()

# Get and peform desired action

print("\n\nWhat would you like to do with " + currentPet.name + "?")

actionMenuNumber = 1
for action in petActions:
	print(str(actionMenuNumber) + " " + action)
	actionMenuNumber += 1

actionChoice = int(input("number: "))
actionType = petActions[actionChoice-1]
getattr(currentPet, actionType)()

