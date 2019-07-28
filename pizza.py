#!/usr/local/bin/python3.7
pizzas = ['cheese', 'pepperoni', 'meat', 'garlic']
friend_pizzas = pizzas[:]

for pizza in pizzas:
    print("Would you like a " + pizza.title() + " Pizza?\n")

print("There are so many different pizzas to choose from here!")
print("Go ahead... Stick the pizza in your butt.")
print("That's it. Who's a dirty pizza lover? You are!\n")

pizzas.append('angeles pokpok')
friend_pizzas.append('bangkok pokpok')

print(pizzas)
print(friend_pizzas)

print("My favorite pizzas are:")
for fav in pizzas:
    print(fav)

print("\nMy friend's favorite pizzas are:")
for ffav in friend_pizzas:
    print(ffav)

# Store information about a pizza being ordered.
pizza = {
    'crust': 'think',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#Summerize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
        "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
