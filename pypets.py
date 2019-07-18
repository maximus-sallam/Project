## Set availabel pet types and actions
petTypes = ('dog', 'cat', 'rabbit', 'lizzard', 'bird', 'fish')
petActions = ('feed', 'walk', 'play', 'sleep', 'nap') 

## Get player name and pet type
playerName = input("Welcome to pypets! \nWhat is your name? ").title()
print("what kind of pet would you like?")
typeMenuNumber = 1
for types in petTypes:
    print(str(typeMenuNumber) + " " + types)
    typeMenuNumber += 1

typeChoice = int(input("number: "))
petType = petTypes[typeChoice-1]

## Pet Classes
class Dog():
    """Dog class"""

    def __init__(self, name, owner):
        """Initialize name and age attributes"""
        self.name = name
        self.owner = owner

    def feed(self):
        """Dog eats"""
        print(self.name + " eats what you gave them.")
    
    def walk(self):
        """Walk dog"""
        print("You take " + self.name + " for a walk.")

    def play(self):
        """Dog plays"""
        print("You play with" + self.name + ".")

    def sleep(self):
        """Dog sleeps"""
        print(self.name + " sleeps.")

    def nap(self):
        """Dog naps"""
        print(self.name + " takes a nap.")

class Cat():
    """Cat class"""

    def __init__(self, name, owner):
        """Initialize name and age attributes"""
        self.name = name
        self.owner = owner

    def feed(self):
        """Cat eats"""
        print(self.name + " eats what you gave them.")
    
    def walk(self):
        """Walk Cat"""
        print(self.name + " doesn't what to go for a walk. it's a cat, dummy")

    def play(self):
        """Cat plays"""
        print("You play with" + self.name + ".")

    def sleep(self):
        """Cat sleeps"""
        print(self.name + " sleeps.")

    def nap(self):
        """Cat naps"""
        print(self.name + " takes a nap.")

##End of pet classes

## Sorry, alpha
if typeChoice == 1:
    petName = input("What would you like to name your " + petType +"?")
    player_dog = Dog(petName, playerName)
    print("\n\nOk, " + player_dog.owner + " your new " + petType + " is named " + player_dog.name + "!")
    print("\n\nWhat would you like to do with " + player_dog.name + "?")    
    currentPet = player_dog
elif typeChoice == 2:
    petName = input("What would you like to name your " + petType +"?")
    player_cat = Cat(petName, playerName)
    print("\n\nOk, " + player_cat.owner + " your new " + petType + " is named " + player_cat.name + "!")
    print("\n\nWhat would you like to do with " + player_cat.name + "?")
    currentPet = player_cat
else:
    print("Sorry, pypets is in alpha. Only dogs and cats are supported at this time")
    exit()

# Get and peform desired action
actionMenuNumber = 1
for action in petActions:
    print(str(actionMenuNumber) + " " + action)
    actionMenuNumber += 1

actionChoice = int(input("number: "))
actionType = petActions[actionChoice-1]
getattr(currentPet, actionType)()

