def print_animals(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "\nSorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        print("\nFile: " + filename + "\n" + contents)

filenames = ['hamsters.txt', 'cats.txt', 'dogs.txt', 'fish.txt']


for filename in filenames:
    print_animals(filename)