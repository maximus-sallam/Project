class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_retaurant(self):
        print("\nWelcome to " + self.restaurant_name.title() + "!")
        print("Our specialty is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open for business.")

pokpokpalace = Restaurant('pokpok palace', 'pleasing you')
vaginaisland = Restaurant('vagina island', 'puki')
hookerfarms = Restaurant('hooker farms', 'riding your dick')
girlsgalore = Restaurant('girls galore', 'making your penis happy')

print(pokpokpalace.restaurant_name)
print(pokpokpalace.cuisine_type)

pokpokpalace.describe_retaurant()
pokpokpalace.open_restaurant()

vaginaisland.describe_retaurant()
vaginaisland.open_restaurant()

hookerfarms.describe_retaurant()
hookerfarms.open_restaurant()

girlsgalore.describe_retaurant()
girlsgalore.open_restaurant()