import json

filename = 'favorite_number.json'
message = "I know your favorite number! It's "
try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    print("No file found.")
except:
    print("The file is empty.")
else:
    print(message + str(numbers) + ".")