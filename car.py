class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_gas_tank(self):
        """Read how full the gas tank is."""
        if self.gas_tank == 0:
            print("The gas tank is empty.")
        else:
            print("The gas tank is " + str(self.gas_tank) + "% full.")

    def fill_gas_tank(self):
        """Fill the gas tank to 100%"""
        if self.gas_tank == 100:
            print("The gas tank is already full.")
        else:
            self.gas_tank = 100
            print("The gas tank is now full.")

    def increment_gas_tank(self, gallons):
        if gallons > self.gas_tank:
            print("You need more gas to go that far.")
        else:
            self.gas_tank = self.gas_tank - gallons
            print("You used " + str(gallons) + " gallons of gas.")
        self.read_gas_tank()


    def drive_somewhere(self, miles):
        """Drive to a random place."""
        if self.gas_tank == 0:
            print("You need gas before you can go anywhere.")
        elif miles > self.gas_tank:
            print("That's too far.")
        else:
            self.increment_gas_tank(miles)
            self.increment_odometer(miles)
            print("You drove " + str(miles) + " miles in a random direction.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initializes attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")



# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.read_gas_tank()
my_used_car.read_odometer()
my_used_car.fill_gas_tank()
my_used_car.drive_somewhere(25)
my_used_car.drive_somewhere(35)
my_used_car.drive_somewhere(20)
my_used_car.read_odometer()
my_used_car.drive_somewhere(25)

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# """Attempting to roll the odometer back."""
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.update_odometer(22)
# my_new_car.read_odometer()