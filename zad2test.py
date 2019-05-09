def pozostale(liczby, n):
    lista = []
    for i in range(1, n + 1):
        if i not in liczby:
            lista.append(i)
    return lista

print(pozostale([2, 4, 5, 7], 10))
