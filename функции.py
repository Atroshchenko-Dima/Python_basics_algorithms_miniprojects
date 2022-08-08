def greet_user(username):
    print(f"Hello {username}!")
greet_user('Dima')

def favorite_book(name):
    print(f"Одна из моих любимых книг это '{name}'!")
favorite_book('1984')
favorite_book('Атлант расправил плечи')
# 8.3
def make_shirt(размер = 'L', текст = 'I love Python'):
    print(f"На этой футболке с размером {размер} нанесен текст '{текст}'")
make_shirt()


"""
def get_formatted_name(first_name, last_name):
#Возвращает аккуратно отформатированное полное имя
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def city_country(city, country):
    full = f"{city} {country}"
    return full
musician = city_country(input(), input())
print(musician) """


def print_models(unprinted_designs, completed_models):
    # Имитируется печать моделей, пока список не станет пустым. 
    # Каждая модель после печати перемещается в completed_models
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Priting model {current_designs}")
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    # Выводит информацию обо всех напечатанных моделях
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot', 'dron']
comleted_models = []

print_models(unprinted_designs, comleted_models)
show_completed_models(comleted_models)


def make_hotdog(*topings):
    print(f"Выберите компоненты хот дога")
    for toping in topings:
        print(f" - {toping}")
make_hotdog('сосиска', "огурец", "перец")