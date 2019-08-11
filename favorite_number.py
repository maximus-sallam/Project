import json

filename = 'favorite_number.json'

def get_stored_number():
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    number = int(input("What is your favorite number? "))
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number

def greet():
    number = get_stored_number()
    if number:
        print("I know your favorite number! It's " + str(number) + ".")
    else:
        number = get_new_number()
        print("We'll remember that your favorite number is " + str(number) + "!")

greet()