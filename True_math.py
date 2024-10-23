
def divide(first, second):
    from math import inf
    if second == 0:
        return inf
    res = first / second
    return res


#print(divide(6, 1))