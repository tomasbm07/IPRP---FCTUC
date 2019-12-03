import random as r
nums = [1, 2, 3, 4, 5, 6]

def dados(quantidade):
    count = 0
    print('\tDado 1\t\tDado2')
    for i in range(quantidade):
        dado_1 = r.choice(nums)
        dado_2 = r.choice(nums)
        soma = dado_1 + dado_2
        print('{}: {}\t\t{}'.format(i+1, dado_1, dado_2))
        if soma % 2:
            count += 1
    percent = count/quantidade
    print('Saiu numero par %.1f%s das vezes' % (percent*100, '%'))


dados(int(input('Numero de lançamentos: ')))
