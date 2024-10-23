def calculate_structure_sum(summa):
    num = 0
    for i in summa:
        if isinstance(i, (list, tuple, set)):
            num += calculate_structure_sum(i)
        elif isinstance(i, dict):
            num += calculate_structure_sum(i.items())
        elif isinstance(i, str):
            num += len(i)
        elif isinstance(i, (int, float)):
            num += i
    return num


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)