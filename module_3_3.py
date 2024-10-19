def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)


# Часть 1
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

# часть 2
values_list = [55, True, 'command']
values_dict = {'a': 1, 'b': 'str', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# Часть 3
values_list_2 = [54.32, 'string']
print_params(*values_list_2, 42)
