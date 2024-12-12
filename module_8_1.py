def add_everything_up(a,b):
    try:
       result = a + b
    except TypeError:
        print(f'разные типы данных, нельзя складывать: {a},{b}')
        return
    else:
        print(f'ура типы данных совпадают: {a},{b}')
        return result


result1 = add_everything_up(123.456, 'строка')
result2 = add_everything_up('яблоко', 4215)
result3 = add_everything_up(123.456, 7)