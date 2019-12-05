receitas = {'sonhos': ['agua', 'farinha', 'manteiga', 'ovos', 'acucar'],
            'rabanadas': ['pao', 'leite', 'ovos', 'manteiga', 'acucar'],
            'leite creme': ['acucar', 'farinha', 'ovos', 'leite']}

ingredientes = {}
keys = list(receitas.keys())
values = list(receitas.values())
# print(keys)
# print(values)

for i in range(len(keys)):
    for j in range(len(values[i])):
        ingredientes[values[i][j]] = ingredientes.get(values[i][j], []) + [keys[i]]
# print(ingredientes)


def ingredientes_mais_usados(dicio):
    keys = list(dicio.keys())
    values = list(dicio.values())
    # print(keys)
    # print(values)
    size = []
    final = {}

    for i in range(len(values)):
        size.append(len(values[i]))
    print(size)
    maxi = max(size)

    for i in range(len(values)):
        if len(values[i]) == maxi:
            final[keys[i]] = final.get(keys[i], []) + values[i]
    print(final)


ingredientes_mais_usados(ingredientes)
