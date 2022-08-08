"""
class Dog(): # Простая модель собаки
    # Обязательно передаем self перед остальным аргументами
    def __init__(self, name, age): # этот метод вызывается автоматически при использовании класса
        # (обязательно два подчеркивания с обоих сторон)
        self.name = name # Инициализирует атрибуты name и age
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting") # Собака садится по команде
    def roll_over(self):
        print(f"{self.name} roller over!") # Собака перекатывается по команде 
        

my_dog = Dog('willie', 6)
your_dog = Dog('Lucy', 4)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog's name is {your_dog.age}")
your_dog.roll_over() """

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"Один из моих любимых ресторанов это {self.restaurant_name}")
        print(f"'{self.restaurant_name}' имеет одну из лучших кухонь в стиле {self.cuisine_type}!")


    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт с 9.00 до 23.00")

    def set_number_served(self):
        print(f"Сегодня в ресторане было {self.number_served} посетителей")  

    def increment_number_served(self, persons):
        self.number_served += persons

class IceCreamStand(Restaurant):

    def __init__(self, type1, type2, type3):
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3

    def describe_flawors(self):
        print(f"в нашем магазине предоставлены эти виды мороженного {self.type1}, {self.type2}, {self.type3}")


my_restaurant = Restaurant("Kaif", 'Минимализм')
your_restaurant = Restaurant("Persona", 'Классика')
my_flawors = IceCreamStand('шоколадное', 'ванильное', "фруктовый лед")
print(my_flawors.describe_flawors())


print(f"{my_restaurant.restaurant_name} - именно тут я люблю проводить свои вечера")
my_restaurant.describe_restaurant()
my_restaurant.number_served = 25
my_restaurant.set_number_served()
my_restaurant.increment_number_served(29)
my_restaurant.set_number_served()


print(f"\n{your_restaurant.restaurant_name} - именно тут я люблю проводить свои вечера")
your_restaurant.describe_restaurant()

