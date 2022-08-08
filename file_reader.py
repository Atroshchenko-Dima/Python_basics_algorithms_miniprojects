a = 'c:\\Users\\Dima\\Desktop\\Python\\pi_digits.txt'
with open(a) as file_object: 
    contens = file_object.read() 
    print(contens.rstrip())
print()

with open(a) as file_object: 
    for line in file_object: 
        print(line.rstrip())
print()
with open(a) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())