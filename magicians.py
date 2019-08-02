def show_magicians(magician_list):
    for magician in magician_list:
        make_great(magician)

def make_great(magician):
    print("The Great " + magician.title())

magicians = ['merlin', 'houdini', 'magical max', 'gandolf the grey', 'ash ketchum']

show_magicians(magicians)