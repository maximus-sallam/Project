responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("What is your name?\n")
    response = input("Where would you like to go on your dream vacation?\n")

    # Store the response in a dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes / no)\n")
    if repeat.lower() == 'n' or repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to vacation to " + response.title())
