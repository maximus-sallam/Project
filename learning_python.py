filename = 'learning_python.txt'

with open(filename) as file_object1:
    print(file_object1.read().replace('Python', 'C'))

with open(filename) as file_object2:
    for line in file_object2:
        print(line.strip().replace('Python', 'C'))

with open(filename) as file_object3:
    lines = file_object3.readlines()
string = '\n'
for line in lines:
    string += line
print(string.replace('Python', 'C'))
