class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age, owner):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.owner = owner

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('riley', 3, 'max')
venice_dog = Dog('bucky', 1, 'venice')
venjovi_dog = Dog('deep fried', 2, 'venjovi')
vennah_dog = Dog('alden', 4, 'vennah')

print("\nThis dog's name is " + my_dog.name.title() + ".")
print("This dog is " + str(my_dog.age) + " years old.")
print(my_dog.name.title() + "'s owner is " + my_dog.owner.title())
my_dog.sit()
my_dog.roll_over()

print("\nThis dog's name is " + venice_dog.name.title() + ".")
print("This dog is " + str(venice_dog.age) + " years old.")
print(venice_dog.name.title() + "'s owner is " + venice_dog.owner.title())
venice_dog.sit()
venice_dog.roll_over()

print("\nThis dog's name is " + venjovi_dog.name.title() + ".")
print("This dog is " + str(venjovi_dog.age) + " years old.")
print(venjovi_dog.name.title() + "'s owner is " + venjovi_dog.owner.title())
venjovi_dog.sit()
venjovi_dog.roll_over()

print("\nThis dog's name is " + vennah_dog.name.title() + ".")
print("This dog is " + str(vennah_dog.age) + " years old.")
print(vennah_dog.name.title() + "'s owner is " + vennah_dog.owner.title())
vennah_dog.sit()
vennah_dog.roll_over()