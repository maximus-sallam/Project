filename = 'moby_dick.txt'
while True:
    try:
        word = input("What word would you like me to look for? ")
        with open(filename) as file:
            contents = file.read()
    except KeyboardInterrupt:
        print("\nDo that one more time to quit!")
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print("The word " + word + " appears " +
            str(contents.lower().count(word)) +
            " times in " + filename)