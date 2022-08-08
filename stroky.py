# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

# print('Я должен сделать', len(shoplist), 'покупки.')

# print('Покупки:', end=' ')
# for item in shoplist:
#     print(item, end=' ')

# print('\nТакже нужно купить риса.')
# shoplist.append('рис')
# print('Теперь мой список покупок таков:', shoplist)

# print('Отсортирую-ка я свой список')
# shoplist.sort()
# print('Отсортированный список покупок выглядит так:', shoplist)

# print('Первое, что мне нужно купить, это', shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print('Я купил', olditem)
# print('Теперь мой список покупок:', shoplist)


topfilms = ['Интерстеллар,','Начало,','Леон']
print('Сегодня я могу посмотреть', len(topfilms), 'фильма')
print('Фильмы', end=' ')
for items in topfilms:
    print(items, end=' ')
print('\nЗавтра я хочу посмотреть еще два фильма')
topfilms.append('Елки')
topfilms.append('Один дома')
print('Теперь мой список выглядит так', topfilms)
print('Отсортирую список по алфавиту')
topfilms.sort()
print("Сегодня я посмотрел 'Интерстеллар'")
del topfilms[0]
print('Список просмотра на завтра', topfilms)