filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contens = f.read()
except FileNotFoundError:
    print(f"Извините, файл {filename} не существует")