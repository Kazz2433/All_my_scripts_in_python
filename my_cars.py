from eletric import Car
from my_eletric_car import EletricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = EletricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())