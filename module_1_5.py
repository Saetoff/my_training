immutable_var = 1, 2, 3, "bonus", type
print(immutable_var)
#immutable_var[0] = 2
#print(immutable_var)
# Тип данных tuple, это не изменяемый тип обьекта в отличий от строк! не поддерживает элемент по обращениям.
mutable_list = ([1, 2], 3, "bonus", type)
mutable_list[0][1] = 5
print(mutable_list)