cities = {
    'manila': {
        'country': 'philippines',
        'population': '12,877,253',
        'fact': 'Metropolitan Manila, officially the National Capital Region, is the seat of government and one of the three defined metropolitan areas of the Philippines.',
    },
    'seoul': {
        'country': 'south korea',
        'population': '9,776,000',
        'fact': 'Seoul, the capital of South Korea, is a huge metropolis where modern skyscrapers, high-tech subways and pop culture meet Buddhist temples, palaces and street markets.',
    },
    'los angeles': {
        'country': 'usa',
        'population': '4,000,000',
        'fact': 'Los Angeles is a sprawling Southern California city and the center of the nation’s film and television industry.',
    },
}

for city, cityInfo in cities.items():
    if cityInfo['country'] == 'usa':
        print("The city of", city.title(), "is located in the", cityInfo['country'].upper())
        print("The population of", city.title(), "is", cityInfo['population'])
        print("Fact about",city.title() + ":", cityInfo['fact'] + "\n")
    elif cityInfo['country'] == 'philippines':
        print("The city of", city.title(), "is located in the", cityInfo['country'].title())
        print("The population of", city.title(), "is", cityInfo['population'])
        print("Fact about",city.title() + ":", cityInfo['fact'] + "\n")
    else:
        print("The city of", city.title(), "is located in", cityInfo['country'].title())
        print("The population of", city.title(), "is", cityInfo['population'])
        print("Fact about",city.title() + ":", cityInfo['fact'] + "\n")
