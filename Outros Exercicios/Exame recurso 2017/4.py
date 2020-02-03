rede = {'tiago': ['rita', 'francisco', 'joao', 'filipa'],
        'joao': ['tiago', 'ricardo'],
        'ricardo': ['rita', 'francisco'],
        'rita': ['tiago', 'filipa', 'ricardo'],
        'filipa': [],
        'francisco': ['tiago']}


def sugestoes(nome, twitter, amigos):
    seguidores = twitter.get(nome)
    sugeridos = list(twitter.keys())
    sugeridos.remove(nome)
    for i in sugeridos:
        if i in seguidores:
            print(i)
            sugeridos.remove(i)

    print(sugeridos)


sugestoes('tiago', rede, 2)
