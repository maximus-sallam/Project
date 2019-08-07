from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print("You rolled a " + str(self.sides) +
              " sided die and rolled a " + str(x))

twenty = Die(20)
nineteen = Die(19)
eighteen = Die(18)
seventeen = Die(17)
sixteen = Die(16)
fifteen = Die(15)
fourteen = Die(14)
thirteen = Die(13)
twelve = Die(12)
eleven = Die(11)
ten = Die(10)
nine = Die(9)
eight = Die(8)
seven = Die(7)
six = Die(6)
five = Die(5)
four = Die(4)
three = Die(3)
coin = Die(2)

twenty.roll_die()