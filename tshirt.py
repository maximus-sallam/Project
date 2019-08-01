# def make_shirt(size='large', text='I love Python'):
#     print("\nYou selected size " + size + ".")
#     print("'" + text + "' will be printed on the shirt.")
#
# make_shirt('small', 'I have to poop')
# make_shirt(size='x-small', text='Eat my pussy')
# make_shirt()
# make_shirt(size='medium')
# make_shirt(size='medium', text="Gotta catch'em all")

def describe_city(city, country='usa'):
    if len(country) <= 4:
        print("\n" + city.title() + " is in the " + country.upper() + ".")
    else:
        print("\n" + city.title() + " is in " + country.title() + ".")

describe_city('bakersfield')
describe_city('manila','philippines')
describe_city('paris', country='france')