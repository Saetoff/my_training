calls = 0


def count_calls(): # подсчитывает вызовы остальных функции
    global calls
    calls += 1
    return


def string_info(string = 'Айнур'): # принимает аргумент - строку и возвращает кортеж из длины этой строки, строку в верхнем регистре и строку в нижнем регистре
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string = str, list1 = list): # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
    count_calls()
    if string in list1:
        return True
    else:
        return False


list_to_search = ['234234', '2343243423', '343', '444', '444333']
i = string_info('one')
print(i)
i = string_info('tho')
print(i)
i = string_info('three')
print(i)

j = is_contains('444', list_to_search)
print(j)
j = is_contains('444333', list_to_search)
print(j)

print(calls)