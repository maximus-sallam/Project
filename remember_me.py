import json

filename = 'username.json'
# Load the username, if it has been stored previously.
#  Otherwise, prompt for the username and store it.

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username.title(), f_obj)
    return username.title()

def remember():
    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")

def maybe():
    username = get_stored_username()
    maybe = input("Are you " + username + "? Enter 'yes' or 'no' ")
    if maybe.lower() == 'yes':
        print("Welcome back, " + username + "!")
    elif maybe.lower() == 'no':
        remember()
    else:
        print("You did not enter a valid response.")
        greet_user()

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        maybe()
    else:
        remember()

greet_user()