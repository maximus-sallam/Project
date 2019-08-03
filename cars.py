#!/usr/local/bin/python3.7

# cars = ['audi', 'bmw', 'suburu', 'toyota']
#
# for car in cars:
#     if (car == 'bmw'):
#         print(car.upper())
#     else:
#         print(car.title())
#
#     if (car == 'suburu'):
#         print('lol')

def build_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = build_car('suburu', 'outback', color='blue', tow_package=True)
print(car)