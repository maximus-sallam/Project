# def city_country(city, country):
#     if len(country) <= 4:
#         formatted = city.title() + ', ' + country.upper()
#     else:
#         formatted = city.title() + ', ' + country.title()
#     return formatted
#
# la = city_country('los angeles', 'usa')
# bako = city_country('bakersfield', 'usa')
# man = city_country('manila', 'philippines')
#
# print(bako)
# print(la)
# print(man)

def make_album(artist, album, tracks=''):
    info = {'artist': artist, 'album title': album}
    if tracks:
        info['tracks'] = tracks
    return info

while True:
    print("CD Database Program")
    print("(enter 'quit' at anytime to quit)")

    album_artist = input("Enter Album Artist: ")
    if album_artist == 'quit':
        break
    album_title = input("Enter Album Title: ")
    if album_title == 'quit':
        break
    album_tracks = input("Optional: Enter number of tracks: ")
    if album_tracks =='quit':
        break

    cd = make_album(album_artist, album_title, album_tracks)
    print(cd)

# cds = [make_album('michael jackson', 'thriller'), make_album('the beatles', 'white album'),
#        make_album('bruno mars', 'giggity'), make_album('spice girls', 'wanna be', 9)]

# for cd in cds:
#     print(cd)