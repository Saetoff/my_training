def get_input():
    number = int(input('Введите число от 3х до 20ти: '))
    if 3 <= number <= 20:
        return number
    return None


def get_shifr(n):
    list = ''
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0:
                list += str(i) + str(j)
    return list

if num := get_input():
    print(get_shifr(num))
else:
    print(f'Не верное число: {num}')
