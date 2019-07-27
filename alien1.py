#!/usr/local/bin/python3.7

alien_0 = {'color': 'green'}
alien_1 = {'color': 'yellow'}
alien_2 = {'color': 'red'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing alients.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green',
                'points': 5,
                'speed': 'slow',
                }
    aliens.append(new_alien)

# Show the first 5 aliiens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
