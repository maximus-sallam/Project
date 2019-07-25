#!/usr/local/bin/python3.7

valid_users = ['admin', 'zebra', 'max', 'joe', 'alex']
entered_users = ['AdmIN', 'ZEBRA', 'mr. potato head', 'MAx', 'captain thunderpants', 'Joe', 'Alex']

welcome = 'Welcome back '
admin = '! Would you like to see a status report?'
other = '! It\'s great to see you again.'
who = 'Who the hell are you, '

for entered_user in entered_users:
    if entered_user.lower() in valid_users and entered_user.lower() == 'admin':
        print(welcome + entered_user.title() + admin)
    elif entered_user.lower() in valid_users:
        print(welcome + entered_user.title() + other)
    else:
        print(who + entered_user.title() + "?!")

