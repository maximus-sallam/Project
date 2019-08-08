#!/usr/local/bin/python3.7

my_foods = ['pizza','burger','cake','pie','tacos']
friend_foods = my_foods[:]

my_foods.append('pokpok')
friend_foods.append('turds')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nThe first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

print("\nThe last three items in the list are:")
print(my_foods[-3:])

for food in my_foods:
    print("\nHave I ever had a " + food + "? Yes, I have!")

for ffood in friend_foods:
    print("\nHave you ever had a " + ffood + "?")


