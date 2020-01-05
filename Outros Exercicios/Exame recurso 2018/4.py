dicio_autor = {'Gomes': ['Harrison', 'Silva', 'Vilela', 'Dinis'],
         'Vilela': ['Harrison', 'Bloch', 'Dalmazo', 'Curado', 'Gomes'],
         'Harrison': ['Bloch', 'Vilela']}


def coautor_todos(dicio):
    new_dicio = {}
    coautores = []
    # Ver quais autores participaram em trabalhos de outros autores
    for keys, values in dicio.items():
        for i in range(len(values)):
            new_dicio[values[i]] = new_dicio.get(values[i], []) + [keys]
    print(new_dicio)

    for i in new_dicio.keys():
        if i in dicio_autor.keys():
            if len(new_dicio.get(i)) == len(dicio_autor.keys()) - 1:
                coautores.append(i)
    print(coautores)


coautor_todos(dicio_autor)
