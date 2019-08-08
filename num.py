#!/usr/local/bin/python3.7
num = 69
message = "My favorite number is " + str(num) + "!"
print(message)

#numbers = list(range(0,999))
#for number in numbers:
#    print(number)

squares = []
for value in range(1,11):
#    square = value ** 2
#    squares.append(square)
    squares.append(value ** 2)
print(squares)

purple = [digit**2 for digit in range(1,11)]
print(purple)

purple = [digit**2 for digit in range(1,11)]
print(purple)

totwenty = list(range(1,21,2))
for twenty in totwenty:
    print(twenty)

million = list(range(1,1000001))
#for mil in million:
#    print(mil)
print(min(million))
print(max(million))
print(sum(million))

cubes_two = []
for cube_two in range(1,11):
    cubes_two.append(cube_two ** 3)
print(cubes_two)

cubes = [cube**3 for cube in range(1,11)]
print(cubes)
