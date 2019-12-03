''''file_nomes = open('Nomes.txt', 'r')
nomes = file_nomes.readlines()
file_nomes.close()

nome = []
genero = []
idade = []

for i in range(len(nomes)):
    nomes[i] = nomes[i].strip('\n').split()

for i in range(len(nomes)):
    nome.append(nomes[i][0])
    genero.append(nomes[i][1])
    idade.append(nomes[i][2])
print(nome)
print(genero)
print(idade)

file_casais = open('Casais.txt', 'w')

for i in range(0, len(nome) - 1):
    if genero[i] != genero[i+1] and (abs(int(idade[i]) - int(idade[i+1]))) <= 5:
        file_casais.write('{}\t{}\n'.format(nomes[i][0], nomes[i+1][0]))
        print('{}\t{}\n'.format(nomes[i][0], nomes[i+1][0]))

file_casais.close()'''''


path = 'Nomes.txt'
path2 = 'Casais.txt'


def casais(ficheiro, valor, novo_ficheiro):
    f = open(ficheiro, 'r')
    ler = f.readlines()
    f.close()
    # ordenar por idades (passo desnecessário mas garante que o maximo de casais possíveis é criado)
    for i in range(len(ler)):
        for j in range(len(ler)-1):
            if ler[j].split()[2] > ler[j+1].split()[2]:
                ler[j], ler[j + 1] = ler[j+1], ler[j]  # troca de ordem na lista
    machos = list()
    femeas = list()
    # separar machos e femeas em duas listas
    for i in ler:
        if i.split()[1] == 'F':
            femeas.append((i.split()[0], i.split()[2]))
        elif i.split()[1] == 'M':
            machos.append((i.split()[0], i.split()[2]))
    # formar casais
    nova_lista = list()
    for m in machos:
        for f in femeas:
            if abs(int(m[1])-int(f[1])) <= valor:
                nova_lista.append(m[0] + ' ' + f[0] + ' ' + str(abs(int(m[1])-int(f[1]))))
                femeas.remove(f)
                break
    # escrever no novo_ficheiro
    f = open(novo_ficheiro, 'w')
    for i in nova_lista:
        f.write(i + '\n')


casais(path, 5, path2)
