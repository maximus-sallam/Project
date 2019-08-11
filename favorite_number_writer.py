import json

filename = 'favorite_number.json'
try:
    number = int(input("What is your favorite number? "))
except ValueError:
    print("That wasn't a number!")
else:
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)