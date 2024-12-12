# простенький файловый менеджер
import tkinter
import os
from fileinput import filename
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)

window = tkinter.Tk() # создаем окно
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black') # цвет заднего фона
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=5, width=65,
                     background='silver', foreground='blue') # размер и цвет секции
text.grid(column=1, row=1) # делим окно на колонны(сетку), и указываем где размещаем колонну
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл',
                               background='silver', foreground='blue',
                                command=file_select)
button_select.grid(column=1, row=2, pady=5)


window.mainloop() # обновляем окно
