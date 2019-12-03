# quantidade comprada inicialmente, preço de compra por kilo, quantidade em stock, preço de venda por quilo

cenas = {0: 'Quantidade comprada inicialmente: ', 1: 'Preço de compra por kilo: ', 2: 'Quantidade em stock: ',
         3: 'Preço de venda por kilo: '}
banana = [100, 5, 50, 6]
pera = [80, 2, 40, 3]
maca = [70, 1, 10, 3]

frutas = {'banana': banana, 'pera': pera, 'maça': maca}
print('---Inicialmente---\n')
print(cenas)
print(frutas)


def edit(fruta):
    fruta.clear()
    for i in range(4):
        fruta.append(int(input('{}'.format(cenas[i]))))
    print(fruta)
    print('O lucro obtido da venda de {} foi de {}€'.format(fruta, profit(fruta)))
    a = True
    return a


def profit(fruta):
    venda = fruta[0] - fruta[2]
    lucro = fruta[1] - fruta[3]
    lucro_total = abs(venda) * abs(lucro)
    return lucro_total


a = True
while a:
    editar = input('Digite a fruta que quer editar: ')
    if editar == 'banana':
        a = edit(banana)

    elif editar == 'pera':
        a = edit(pera)

    elif editar == 'maça':
        a = edit(maca)
