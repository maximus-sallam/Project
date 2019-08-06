import restaurant

my_resto = restaurant.IceCreamStand('massagy boom boom', 'rubbing your dick')
my_resto.describe_retaurant()
my_resto.open_restaurant()
my_resto.display_flavors()

pokpokpalace = restaurant.Restaurant('pokpok palace', 'pleasing you')
vaginaisland = restaurant.Restaurant('vagina island', 'puki')
hookerfarms = restaurant.Restaurant('hooker farms', 'riding your dick')
girlsgalore = restaurant.Restaurant('girls galore', 'making your penis happy')

print(my_resto.number_served)
my_resto.number_served = 23
my_resto.set_number_served(21)
my_resto.set_number_served(25)
print(my_resto.number_served)
my_resto.increment_number_served(25)
print(my_resto.number_served)


pokpokpalace = restaurant.Restaurant('pokpok palace', 'pleasing you')
vaginaisland = restaurant.Restaurant('vagina island', 'puki')
hookerfarms = restaurant.Restaurant('hooker farms', 'riding your dick')
girlsgalore = restaurant.Restaurant('girls galore', 'making your penis happy')

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