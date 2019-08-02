def show_magicians(magician_list):
    while magician_list:
        current_magician = magician_list.pop()
        print(current_magician)



magicians = ['merlin', 'houdini', 'magical max', 'gandolf the grey', 'ash ketchum']
great_magicians = []

show_magicians(magicians)