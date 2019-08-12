def city_country(city, country, population=''):
    """Generate a neatly formatted sentence about a city and country."""
    if population:
        where_is = 'The city of ' + city.title() + \
               ' is in the country of ' + country.title() + \
               '.\nThe population of ' + city.title() + ', ' + \
               country.title() + ' is ' + str(population) + '.'
    else:
        where_is = 'The city of ' + city.title() + \
                   ' is in the country of ' + country.title() + '.'
    return where_is