filename = 'programming_poll.txt'

while True:
    prompt = input("Why do you like programming? ") + "\n"
    print("Thanks for taking our poll!")
    with open(filename, 'a') as file_object:
        file_object.write(prompt)