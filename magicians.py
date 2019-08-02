magicians = ['merlin', 'houdini', 'magical max', 'gandolf the grey', 'ash ketchum']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    count = 0
    for magician in magicians:
        magicians[count] = 'the great ' + magician
        count += 1
    return magicians

show_magicians(make_great(magicians))

# show_magicians(magicians)
# make_great(magicians)
# show_magicians(magicians)