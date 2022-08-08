"""
class Car(): # Простая модель автомобиля.


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # Возвращает аккуратно отформатированное описание
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer() """

"""
class Car(): # Простая модель автомобиля.


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # Возвращает аккуратно отформатированное описание
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage # устанавливает заданное значение на одометре

    def increment_odometer(self, miles):
        #Увеличивает показания одометра с заданным приращением
        self.odometer_reading += miles
        

my_used_car = Car('audi', 'a4', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer() """


class Car(): # Простая модель автомобиля.


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # Возвращает аккуратно отформатированное описание
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage # устанавливает заданное значение на одометре

    def increment_odometer(self, miles):
        #Увеличивает показания одометра с заданным приращением
        self.odometer_reading += miles


class Battery():
    # Простая модель аккумулятора(мы можем переместить все методы и атрибуты касающиеся батареи в отдельный класс)

    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        # Выводит информацию о мощности аккумулятора
        print(f"This car has a {self.battery_size} kWh battery.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size != 100:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")
     

    def get_range(self):
        # выводит приблизительный запас хода для аккумулятора
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315 
        print(f"Эта машина может проехать около {range} миль на полной зарядке")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        # Инициализирует атрибуты класса - родителя, затем инициализирует атрибуты, специфические для электромобиля
        super().__init__(make, model, year) # super - специальная функция способная вызвать метод родительского класса(Car) 
        self.battery = Battery()


my_tesla = ElectricCar('tesla', ' model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
