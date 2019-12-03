import random

f = open('Names.txt', 'r')
nomes = f.readlines()
f.close()

for i in range(len(nomes)):
    nomes[i] = nomes[i].strip('\n')


def twitter(tamanho):
    twitter_dicio = {}
    keys = [nomes[a] for a in range(tamanho)]
    values = [[nomes[random.randint(0, len(nomes) - 1)] for b in range(random.randint(0, len(nomes)))] for c in range(tamanho)]
    twitter_dicio = dict(zip(keys, values))
    return twitter_dicio


def followers(dicio):
    keys = list(dicio.keys())
    values = list(dicio.values())
    size = [0 for d in keys]
    for l in range(len(values)):
        size[l] = len(values[l])

    for k in range(len(values)):
        if values[k] == max(values):
            size = [keys[k], len(values[k])]

    print('{} tem {} followers, sendo o que tem mais followers de {} pessoas.'.format(size[0], size[1], len(keys)))


# numero maximo = numero de nomes no ficheiro com os nomes. 1000
followers(twitter(500))

