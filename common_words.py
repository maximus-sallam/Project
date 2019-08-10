filename = 'moby_dick.txt'
while True:
    word = input("What word would you like me to look for? ")
    with open(filename) as file:
        contents = file.read()
    print("The word " + word + " appears " +
          str(contents.lower().count(word)) +
          " times in " + filename)
