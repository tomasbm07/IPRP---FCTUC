
def conta_menores(num, list):
    cont = 0
    for i in range(len(list)):
        if (list[i] < num):
            cont += 1
    print('{} numeros da lista, sao menores que {}'.format(cont,num))

conta_menores(5, [1, 2, 3, 4, 5, 6, 7])