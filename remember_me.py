# Импорт модуля os
import os

# Печать текущего рабочего каталога
print("Текущий рабочий каталог: {0}".format(os.getcwd()))

# Изменение текущего рабочего каталога
os.chdir('C:\\Users\\Dima\\Desktop\\Python')

# Печать текущего рабочего каталога
print("Текущий рабочий каталог: {0}".format(os.getcwd()))


import json
# Программа загружает имя пользователя, если оно не было сохранено ранее
# В противном случае она запрашивает имя пользователя и сохраняет его
def get_stored_username():
    # Приветсвует пользователя по имени
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    #Запрашивает новое имя пользователя
    username = input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)

def greet_user():
    username = get_stored_username()
    if username:
        print(f"welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"Будем ждать когда ты вернешься, {username}!")

greet_user()