car = input("What kind of rental car would you like? ")
print("Let me see if I can find you a", car.title())

seats = int(input("How many people are in your dinner group? "))
if (seats > 8):
    print("I'm afraid you'll need to wait for a table.")
else:
    print("Your table is ready.")

number = int(input("Please type any number: "))
if number % 10 == 0:
    print("This number is a multiple of 10")
else:
    print("This number is not a multiple of 10")