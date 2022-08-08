numbers = 'c:\\Users\\Dima\\Desktop\\numbers.txt'
counter = 0
# из блокнота сразу в числовой массив
with open(numbers) as f: 
    list = [int(item) for item in f]
# подсчет    
for i in range(len(list)-1):
    if list[i+1] > list[i]:
        counter += 1
print(list)
print(counter)
