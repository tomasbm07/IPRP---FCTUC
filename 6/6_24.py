def simetrico(c_1, c_2):
    conj = set()
    for elem_1 in c_1:
        for elem_2 in c_2:
            conj.add((elem_1, elem_2))
    return conj


print(simetrico([1, 2], [3, 4]))
