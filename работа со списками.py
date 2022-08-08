magicians = ['alice', 'david', "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a grat trick!")
    print(f"I cant wait to se your new trick, {magician.title()}\n")
print(f"Thank you everyone")

numbers = list(range(0,11,2)) # создаем массив
print(numbers)

squares = [value**2 for value in range(1,11,2)]
print(squares)

a = list(range(1000000))
print(max(a)) 

menu = ("утка по пекински", "лобстер", "краб", "уха", "щи")
menu = ("утка по пекински", "уха", "щи")
for i in menu:
    print(i)