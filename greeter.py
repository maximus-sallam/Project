# def greet_user(username):
#     """Display a simple greeting."""
#     print("Hello, " + username.title() + "!")

# greet_user(input("What is your name? "))

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\n Hello, " + formatted_name + "!")