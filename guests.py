#!/usr/local/bin/python3.7
guests = [ 'Albert Einstein', 'Thomas Edison', 'Nikola Tesla', 'Elon Musk' ] # This is my list of guests

num = len(guests) # This is how many guests are in the list
i = 0
while i < num: # This itterates through each guest and prints the guests name with a message
    print("Please come over and eat my food, " + guests[i])
    i = i + 1

print("") # This is white space
print("Oh dear! It appears that " + guests[2] + " won't be joining us.")

cant = guests.pop(2) # This removes Nikola Tesla from the list and stores it as cant
guests.insert(2, 'Alexander Shulgin') # Inserts guest into the 2 position
print("") # This is white space

i = 0
while i < num: # This itterates through each guest and prints the guests name with a message
    print(guests[i] + ", I've found a bigger table!")
    i = i + 1

guests.insert(0, 'Richard Feynman') # Adds guest to the beginning of the list
guests.insert(3, 'Pablo Escobar') # Inserts guest into the 3 position
guests.append('Freddy Krueger') # Appends guest to the end of the list
num = len(guests)
print("") # This is white space

i = 0
while i < num: # This itterates through each guest and prints the guests name with a message
    print("Please come over and eat my food, " + guests[i])
    i = i + 1

print("") # This is white space
print("Oh dear! The Hulk smashed the table and now I can only invite two people")

print("")
sorry = guests.pop()
print("Sorry " + sorry + ". You're no longer invited")
sorry = guests.pop()
print("Sorry " + sorry + ". You're no longer invited")
sorry = guests.pop()
print("Sorry " + sorry + ". You're no longer invited")
sorry = guests.pop()
print("Sorry " + sorry + ". You're no longer invited")
sorry = guests.pop()
print("Sorry " + sorry + ". You're no longer invited")
num = len(guests)
print("")

i = 0
while i < num: #
    print("I hope to see you at dinner, " + guests[i])
    i = i + 1

del guests[0]
del guests[0]
print(guests)
