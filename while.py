# 7.2
"""numbers = int(input("На сколько человек вы бы хотели забронировать столик? "))
if numbers > 8:
    print("Вам придется немного подождать")
else:
    print("Ваш стол забронирован")"""
"""
promt = "\nTell me something, and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program.  "
message = "" # чтобы значение выполнялось без ошибок при 1 выполнении программы
while message != 'quit':    
    message = input(promt)
    print(message)
    if message != 'quit': # чтобы не выводилось слово quit, когда пользователь хочет завершения
        print(message)
"""

promt = "\nTell me something, and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program.  "  

active = True
while active:
    message = input(promt)
    if message == 'quit':
        active = False
    else:
        print(message)


x = 1
while x < 3:
    print(x)