'''# начинаем с 2х списков. Пользователей для проверки и постого списка для хранения уже проверенных
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные пользователи.
# каждый пользователь прошедший проверку, перемещается в список проверенных
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f" Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) '''
"""
responses = {}
# Установка флага продолжения опроса
polling_active = True
while polling_active:
    name = input("\nКак тебя зовут? ")
    response = input("\nКакую гору ты бы хотел покорить? ")
    #ответ сохраняется в словаре
    responses[name] = response
    # Проверка продолжения опроса
    repeat = input("whould you like to let another person respond? (yes or no) ")
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} whould like to climb {response}.") """
# 7.8
sandwich_orders = ["тунец", "немецкий", "английский", "датский", 'pastrami', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches =[]
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_sandwich = sandwich_orders.pop()
    print(f" I made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)
# Вывод всех проверенных пользователей
print("\nThe following users have been confirmed")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7.10
vacation = {}
active = True
name = input("Как тебя зовут? ")
place = input("Где ты хочешь отдохнуь? ")
vacation[name] = place
for name, place in vacation.items():
    print(f"{name.title()} хочет отдохнуть в {place}")