import io
from pprint import pprint # импорт библиотеки позволяющая чтение текста внутри файла

name = 'sample.txt'
file = open(name, 'r', encoding='utf-8') # энкодинг дает кодировку русских символов, по умолчанию ее нет
print(file.writable()) # метод показывает, можем ли мы записывать в файл
print(file.readable()) # метод показывает, можем ли читать файл
print(file.seekable()) # метод показывает, можем ли перемещать курсор в файле
print(file.tell()) # количество символов в байтах
pprint(file.read()) # содержимое файла
print(file.name) # увидим имя файла
print(file.buffer) # увидим определенный баффер
print(file.closed) # если тру, то файл закрыт, фалсе то файл открыт
#file.seek(15) # передвигаем курсор
#file.write('\nnew text') # запись текста в файл
print(file.tell())
file.close()
print(file.closed)