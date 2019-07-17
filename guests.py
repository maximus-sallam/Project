#!/usr/local/bin/python3.7
guests = [ 'Albert Einstein', 'Thomas Edison', 'Nikola Tesla', 'Elon Musk' ]

print("Please come over and eat my food, " + guests[0])
print("Please come over and eat my food, " + guests[1])
print("Please come over and eat my food, " + guests[2])
print("Please come over and eat my food, " + guests[3])

print("Oh dear! It appears that " + guests[2] + " won't be joining us.")

cant = guests.pop(2)
guests.insert(2, 'Alexander Shulgin')

print("Please come over and eat my food, " + guests[0])
print("Please come over and eat my food, " + guests[1])
print("Please come over and eat my food, " + guests[2])
print("Please come over and eat my food, " + guests[3])



