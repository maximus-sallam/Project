users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for userName, userInfo in users.items():
    print("\nUsername: " + userName)
    fullName = userInfo['first'] + " " + userInfo['last']
    location = userInfo['location']

    print("\tFull name: " + fullName.title())
    print("\tLocation: " + location.title())