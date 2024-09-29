my_dict = {"Ainur" : 1990, "Victor" : 1987, "Misha" : 2000}
print("Словарь", my_dict)
print("Existing value:", my_dict["Ainur"])
print("Not existing value:", my_dict.get("Galina"))
my_dict.update({"Katy" : 2005})
print("Modified dictionary:", my_dict)
print("Deleted value:", my_dict.pop("Victor"))

my_set = {1, 2, 3, 1, 2, 3, 4, "string", True, (4, 5, 6)}
print("Set:", my_set)
my_set.update({"222", 9})
print("Modified set:", my_set)
my_set.discard("string")
print("Deleted set:", my_set)