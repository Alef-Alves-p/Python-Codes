# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:


def grow(lista):

    result = 1
    for i in lista:
        result = result * i
    return result

lista = [1, 2, 3, 4]

print(grow(lista))