import car
import electric_car

my_beetle = car.Car('volkswagon', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()