age = int(input("How old are you? "))

if age < 3:
    price = 'free!'
elif age <= 12:
    price = '$10.00'
else:
    price = '$15.00'

print("Your ticket is " + price)