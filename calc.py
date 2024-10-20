import tkinter as tk                        # импортируем библиотеку tkinter и будем обращаться к ней с названием tk


def get_values():                        # возвращающая функция
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):                       # принимает значение value и подставляет вместо ответа
    answer_entry.delete(0, 'end')   # очищаем вывод от предыдущих ответов с индексом от 0 до конца
    answer_entry.insert(0, value)       # вывод ответа, индекс куда будем вставлять ответ, и рес что будем вставлять


def add():
    num1, num2 = get_values()                        #   вызываем функцию
    res = num1 + num2
    insert_values(res)                                  # вызываем функцию и передаем результат


def sub():
    num1, num2 = get_values()                        # вызываем функцию
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()    #  Создаем переменную и вписываем библиотеку тк с классом Тк() в этой переменной будет находиться наше окошко
window.title('Калькулятор') # Название нашего окошка
window.geometry('350x350')   #   Размер нашего окна
window.resizable(False,False) # фиксируем размер окна, что бы нельзя было его растягивать
button_add = tk.Button(window, text='сложение +', width=10, height=2, command=add)    #   Создаем переменную для кнопки, присваиваем его для библиотеки (тк) и даем название
button_add.place(x=70, y=200)  #   Метод place размещает кнопку в окошке по координатам
button_sub = tk.Button(window, text='вычитание -', width=10, height=2, command=sub)  # width - длина кнопки, height - высота кнопки
button_sub.place(x=200, y=200)
button_mul = tk.Button(window, text='умножение *', width=10, height=2, command=mul) # с помощью command привязываем кнопки к функции
button_mul.place(x=70, y=150)
button_div = tk.Button(window, text='деление /', width=10, height=2, command=div)
button_div.place(x=200, y=150)
number1_entry = tk.Entry(window, width=34)  # создаем поле для ввода первого числа
number1_entry.place(x=70, y=50)
number2_entry = tk.Entry(window, width=34)  # создаем поле для ввода второго числа
number2_entry.place(x=70, y=100)
answer_entry = tk.Entry(window, width=34)  # создаем поле для вывода ответа
answer_entry.place(x=70, y=282)
number1 = tk.Label(window, text='Введите первое число:') #   Подписываем виджеты ввода
number1.place(x=70, y=29)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=70, y=79)
answer = tk.Label(window, text='Полученный ответ:')
answer.place(x=70, y=260)
window.mainloop()   # запускаем цикл обновления события, обновляет экран происходящее на экране



