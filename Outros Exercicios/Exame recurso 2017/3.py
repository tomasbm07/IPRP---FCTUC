# carater, posiçao inicial, numero consecutivo de vezes que aparece
lista_tupulos = [('2', 1, 1), ('a', 10, 0), ('x', 0, 0), ('d', 3, 2), (' ', 6, 0), ('c', 7, 0), ('b', 8, 1)]
# x22ddd cbba


def gera_cadeia(lista):
    soma = 0
    string = ''
    for i in range(len(lista)):
        if lista[i][2] == 0:
            soma += 1
        else:
            soma += lista[i][2] + 1

    string_lista = ['' for k in range(soma)]

    for i in range(len(lista)):
        if lista[i][2] == 0:
            string_lista[lista[i][1]] = lista[i][0]
        elif lista[i][2] > 0:
            for j in range(lista[i][2] + 1): 
                if j == 0:
                    string_lista[lista[i][1]] = lista[i][0]
                else:
                    string_lista[lista[i][1] + j] = lista[i][0]

    for i in string_lista:
        string += i

    return string


print(gera_cadeia(lista_tupulos))


