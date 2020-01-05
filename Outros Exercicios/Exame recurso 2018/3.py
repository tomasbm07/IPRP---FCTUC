# nome, peso por palete, lucro
lista_carga = [('arroz', 40, 100), ('alface', 60, 200), ('batata', 60, 200), ('cenoura', 120, 250)]
dentro_peso = []


def melhor_peso(carga, peso_max):
    for j in range(len(carga)):
        if carga == []:
            return dentro_peso
        if carga[0][1] + carga[j][1] <= peso_max:
            dentro_peso.append([(carga[0][0], carga[j][0]), (carga[0][2], carga[j][2])])
        if j == len(carga) - 1:
            return melhor_peso(carga[1:], peso_max)
    return dentro_peso


# 2 paletes e não exceder o valor defenido. podem ser repetidas paletes do mesmo tip. Lucro máximo
def melhor_carga(carga, peso_max):
    lucro_max = 0
    lista_peso = melhor_peso(carga, peso_max)
    for i in range(len(lista_peso)):
        for j in range(len(lista_peso[1])):
            if lista_peso[i][1][0] + lista_peso[i][1][1] >= lucro_max:
                lucro_max = lista_peso[i][1][0] + lista_peso[i][1][1]
                objeto = (lista_peso[i][0][0], lista_peso[i][0][1])
    print(objeto)


melhor_carga(lista_carga, 100)


