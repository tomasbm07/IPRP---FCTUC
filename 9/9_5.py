
def conjuntos(conj1, conj2):
    if not conj1:  # conj1 == []
        return True
    elif conj1[0] == conj2[0]:
        return conjuntos(conj1[1:], conj2[1:])
    elif conj1[0] != conj2[0]:
        return conjuntos(conj1, conj2[1:])
    else:
        return False


print(conjuntos([1, 2, 3], [8, 1, 2, 3, 5, 6]))
