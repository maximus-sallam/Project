def city_country(city, country):
    """Generate a neatly formatted sentence about a city and country."""
    where_is = 'The city of ' + city.title() + \
               ' is in the country of ' + country.title() + '.'
    return where_is