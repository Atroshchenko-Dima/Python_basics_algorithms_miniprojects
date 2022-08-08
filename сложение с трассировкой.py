a, b = (input("Введите первое число ")), (input("Введите второе число "))
while True:
    try:
        answer = int(a) + int(b)
    except ValueError:
        print('Нужно указать числа')
    else:
        print(a, '+', b, '=', answer)