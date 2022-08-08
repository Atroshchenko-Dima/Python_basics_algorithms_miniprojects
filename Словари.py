""" alien_0 = {"color": "green", "points" : 5}
new_points = alien_0["points"]
print(f"Ты получил {new_points} очков!")

alien_0["x_position"] = 0
alien_0["y _position"] = 25
print(alien_0) """

"""alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")
alien_0["color"] = "yellow"
print(f"The alien is {alien_0['color']}.") """

"""alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

# Пришелец перемещается вправо
# Вычисляем величину смещения на основании текущей скорости
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment # Новая позиция = сумме старой позиции и приращения
print(f"New position: {alien_0['x_position']}")"""

"""
favorite_language = {
    'jen': 'python', 
    'sarah': 'ruby', 
    'jho': 'C'
    }
language = favorite_language["sarah"].title()
print(f"Любимый язык сары это {language}")

name = {
    'Имя': 'Dima, студент, ученик это пава аывфывфы ......', 
    'Фамилия': 'Атрощенко', 
    'возраст': '23'
    }

print(name["Имя"])
print(name["возраст"])  """
"""
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items(): #возвращает список пар ключ-значение
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_language = {
    'jen': 'python', 
    'sarah': 'ruby', 
    'jho': 'C'
    }
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

countries = {'Египет': 'Нил', 'США': 'Мичиган', 'ЮАР': 'Лимпопо'}
for reka, countrie in countries.items():
    print(f"В {reka} течет река {countrie}")
# создание 30 пришельцев
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'speed': 'slow'}
    aliens.append(new_alien)
# вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)
print('...') 
# вывод кол-ва созданных пришельцев
print(f"Total number of aliens: {len(aliens)} ") """
"""
people = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

people1 = {
    'username': 'dima98',
    'first': 'dima',
    'last': 'atroshenko',
    }
people2 = {
    'username': 'pasha75',
    'first': 'pasha',
    'last': 'atroshenko',
    }
#6.7
sum_people = [people, people1, people2]
for i in sum_people:
    print(i)
# 6.8
animal1 = {
    'kind': 'cat',
    'name': 'busya',
    }
animal2 = {
    'kind': 'dog',
    'name': 'bum',
    }
animal3 = {
    'kind': 'mouse',
    'name': 'dudles',
    }
pets = [animal1, animal2, animal3]
for i in pets:
    print(i)"""

#6.10
numbers = {
    'Dima': [7, 5],
    'Pasha': ['book','cook'],
    'Ivan': [2, 9],
    'Andrew': "5",
    }
for name, number in numbers.items():
    print(f"\nЛюбимое число {name.title()} это")
    for num in number:
        print(f"\t{num}")