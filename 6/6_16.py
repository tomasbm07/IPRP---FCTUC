
dicio = {}


def posicoes(string):
    for i, car in enumerate(string):
        # print(i, car)
        if car in 'aeiouAEIOU':
            dicio[car] = dicio.get(car, []) + [i]
    return dicio


print(posicoes('agora e que vao ser elas, Ai, Ai!'))

