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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate']

    def display_flavors(self):
        print("Our available flavors are:")
        for flavor in self.flavors:
            print("- " + flavor.title())