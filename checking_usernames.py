#!/usr/local/bin/python3.7

current_users = ['maxipad007', 'maximus007', 'maxalot007', 'maxlovesven007', 'penisvagina', 'pokpoklover5000', 'angelescity4ever']
new_users = ['goobybooby23', 'poopmonster432', 'he_is_a_pooper', 'thedogpoops22', 'omgpoop', 'POKPOKlover5000', 'ANGELEScity4ever']
#new_users = []

taken = " is taken. You will need to enter a different username"
nottaken = " is available"
error = "An error has occured"
no = "No username entered"

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(new_user + taken)
        elif new_user.lower() not in current_users:
            print(new_user + nottaken)
        else:
            print(error)
else:
    print(no)
