tree = {'ernesto': ['ana', 'joana', 'tiago'], 'ana': ['joao', 'joel']}


def netos(dicio):
    keys = list(dicio.keys())
    data = list(dicio.values())
    print(keys)
    print(data)
    for i in keys:
        for j in data:
            if i == j:
                print('{} tem um neto'.format(i))
            else:
                print('NADA')


netos(tree)
