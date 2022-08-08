# def say():
#     print("Hello world")
# say()
# say()
# say()

# def printMax(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'максимально')
# printMax(3, 3) # прямая передача значений
# x = 5
# y = 7
# printMax(x, y)

# def person(surname, name, age):
#     names = f"{surname} {name}", float(age)
#     print(names)

# person("Atroshenko", "Dima", 2.2)

# def fibonachi(abc):

#     a=b=1
#     for i in range(1,abc):
#         a, b = b, a+b
#         print(a)

# fibonachi(10)







# a=0
# for i in list(range(1000)):
#     if i % 3 == 0 and i % 5 == 0:
#         a+=i
#         print(a)

def sum(abc):
    
    for i in range(1, 600851475143):

        if abc % i == 0 and abc % abc == 0 and abc % 1 == 0 and i > 100000:
            print(i)

sum(600851475143)

