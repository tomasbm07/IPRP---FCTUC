linhas  = int(input('Digite o nº de linhas da tabela: '))
print('Numero | Quadrado')
for i in range(linhas):
    x = (i+1)**2
    print('{0:6} {1:6}'.format(i+1, x))