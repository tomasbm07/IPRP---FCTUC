def prep_file(ficheiro):
    file = open(ficheiro, 'r')
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n').split('|')
        lines[i][2] = lines[i][2].split(',')
    return lines


def publicacoes_conjuntas(ficheiro, autor):
    lines = prep_file(ficheiro)
    pubs = []
    for i in range(len(lines)):
        if autor in lines[i][2]:
            pubs.append([lines[i][0], lines[i][1]])

    pubs_final = ['' for i in range(len(pubs))]

    for i in range(len(pubs)):
        pubs_final[i] = '{}-{}'.format(pubs[i][0], pubs[i][1])

    print(pubs_final)


publicacoes_conjuntas('Ficheiro.txt', 'Mendes')
