from pprint import pprint

name = 'sample.txt'
file = open(name, 'r') # r- read, w - write, a - append
#print(file)
#pprint(file.read()) # чтение файла
#file.write('hello world') # перезапись файла
#file.write("\nhello world444") # добавление текста в файл

print(file.tell()) # показывает общее количество символов
pprint(file.read()) # показывает, где находиться курсор
print(file.seek(25)) # передвигаем курсор на 25-й символ
pprint(file.read()) # читает что находиться на 25 - ом месте
file.close() # закрыть файл для сохранения изменений

