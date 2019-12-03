linhas = int(input('Digite o numero de linhas da matriz: '))
colunas = int(input('Digite o numero de colunas da matriz: '))

print('--Digite os valores separados por um espaço--')
print('Digite os valores de uma matriz {} x {}'.format(linhas, colunas))
matrix = [(input('Linha {}: '.format(i + 1)).split()) for i in range(linhas)]


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def transposta(matrix):
    print('\n---Matriz introduzida---')
    represent(matrix)
    # convert(matrix)
    # new_matrix = [[0 for elem in linha] for linha in matrix]
    new_matrix = [[0 for i in range(linhas)] for i in range(colunas)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = (matrix[i][j])
    # print(new_matrix)
    print('\n---Matriz transposta---')
    represent(new_matrix)


def represent(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


transposta(matrix)
