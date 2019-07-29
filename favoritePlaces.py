favorite_places = {
    'joe': ['new york', 'michigan', 'sweden'],
    'alex': ['texas', 'hell', 'michigan'],
    'camron': ['louisiana', 'philippines', 'california'],
    'cortney': ['sweden', 'michigan', 'california'],
}

for name in favorite_places:
    print(name.title() + "'s favorite places are", ", ".join(favorite_places[name]).title())