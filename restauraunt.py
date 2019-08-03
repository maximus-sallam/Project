class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_retaurant(self):
        print("\nWelcome to " + self.restaurant_name.title() + "!")
        print("Our specialty is " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open for business.")

restaurant = Restaurant('pokpok palace', 'puki')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_retaurant()
restaurant.open_restaurant()
