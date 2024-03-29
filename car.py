"""A class that can be used to represent a car."""

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
        """Adjust the gas tank based on distance traveled."""
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
        # elif miles > self.gas_tank:
        #     print("That's too far.")
        else:
            print("You drove " + str(miles) + " miles in a random direction.")
            self.increment_odometer(miles)
            self.increment_gas_tank(miles)