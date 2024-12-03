name = 'test.txt'

with open(name, encoding='utf-8') as file:  # оператор вис открывает файл, выполняет манипуляций с файлом и закрывает его сам, указывать закрытие файла не требуется
    for line in file:
        #print(line, end='')
        for char in line:
            print(char)
    print(file.tell())
