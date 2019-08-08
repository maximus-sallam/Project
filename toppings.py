#!/usr/local/bin/python3.7
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")


#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni")
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")

prompt = "What would you like on your pizza?\n"
prompt += "Enter 'quit' or 'exit' to exit\n"

while True:
    topping = input(prompt)

    if topping == 'quit' or topping == 'exit':
        print("Your pizza is finished!")
        break
    elif topping == "":
        print("You didn't select a topping")
    else:
        print("I'm adding " + topping + " to your pizza now.\n")
