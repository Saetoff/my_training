def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1 and int(str_number[1:]) > 0:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(int('40203'))
print(result)
result = get_multiplied_digits(int('40200'))
print(result)
result = get_multiplied_digits(int('042'))
print(result)