def make_sandwich(*items):
    print("\nYou ordered a sandwhich with:")
    if items:
        for item in items:
            print("- " + item)
    else:
        print('Nothing. Your sandwich is just bread.')

make_sandwich('bacon', 'lettuce', 'tomato', 'onion')
make_sandwich('bacon')
make_sandwich()