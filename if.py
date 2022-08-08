massiv = []
if massiv:
    print("hello")
else:
    print("We need some users")


users = ["dima", "ivan", "andrey", "pasha"]
new_users = ["dima1", "ivan1", "andrey", "pasha"]
for user in new_users:
    if user in users:
        print("Такое имя уже есть")
    else:
        print("Это имя доступно")