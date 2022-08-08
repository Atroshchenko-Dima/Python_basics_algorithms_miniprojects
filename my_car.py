from car import Car

my_tesla = Car('audi', 'a4', '2019')
print(my_tesla.get_descriptive_name())

my_tesla.odometer_reading = 23
my_tesla.read_odometer()