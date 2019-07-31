# Start with a list of sandwiches that need to be made.
sandwhich_orders = ['capocolla', 'pastrami', 'dry salami', 'pepperoni',
                    'pastrami', 'ham', 'turkey breast', 'bacon', 'pastrami']
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami, and then
# use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
print("I'm sorry, we're out of pastrami today.")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

# Make each sandwich until there are no more sandwiches that need to be made.
while sandwhich_orders:

    current_sandwich = sandwhich_orders.pop()

    print("Your " + current_sandwich.title() + " sandwich is complete.")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\nThe following sandwiches have been made:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())