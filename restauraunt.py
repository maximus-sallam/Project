class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_retaurant(self):
        print("\nWelcome to " + self.restaurant_name.title() + "!")
        print("Our specialty is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open for business.")

    def set_number_served(self, served):
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't un-serve people!")

    def increment_number_served(self, served):
        self.number_served += served

restaurant = Restaurant('massagy boom boom', 'rubbing your dick')


print(restaurant.number_served)
restaurant.number_served = 23
restaurant.set_number_served(21)
restaurant.set_number_served(25)
print(restaurant.number_served)
restaurant.increment_number_served(25)
print(restaurant.number_served)


pokpokpalace = Restaurant('pokpok palace', 'pleasing you')
vaginaisland = Restaurant('vagina island', 'puki')
hookerfarms = Restaurant('hooker farms', 'riding your dick')
girlsgalore = Restaurant('girls galore', 'making your penis happy')

# print(pokpokpalace.restaurant_name)
# print(pokpokpalace.cuisine_type)
#
# pokpokpalace.describe_retaurant()
# pokpokpalace.open_restaurant()
#
# vaginaisland.describe_retaurant()
# vaginaisland.open_restaurant()
#
# hookerfarms.describe_retaurant()
# hookerfarms.open_restaurant()
#
# girlsgalore.describe_retaurant()
# girlsgalore.open_restaurant()