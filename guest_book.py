filename = 'guest_book.txt'

while True:
    prompt = input("What is your name? ") + "\n"
    print("Hello, " + prompt)
    with open(filename, 'a') as file_object:
        file_object.write(prompt)