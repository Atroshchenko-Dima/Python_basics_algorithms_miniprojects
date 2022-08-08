from car import Car, ElectricCar as EC

my_tesla = EC('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())

my_new_car = Car('audi', 'a4', '2011')
print(my_new_car.get_descriptive_name())


