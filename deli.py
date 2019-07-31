# Start with a list of sandwiches that need to be made.
sandwhich_orders = ['capocolla, dry salami, pepperoni, ham', 'ham, capocolla', 'dry salami, pepperoni', 'ham, dry salami', 'turkey breast, ham']
finished_sandwiches = []

# Make each sandwich until there are no more sandwiches that need to be made.
while sandwhich_orders:
    current_sandwich = sandwhich_orders.pop()

    print("Your " + current_sandwich.title() + " is complete.")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\nThe following sandwiches have been made:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())