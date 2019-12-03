keys = ['Género', 'Idade', 'Altura', 'Peso']
valores = [input('{}: '.format(i)) for i in keys]

dados = {key: value for key, value in zip(keys, valores)}


def metabolismo(dados):
    if dados['Género'] == 'H':
        valor = 66 + (6.3 * float(dados['Peso'])) + (12.9 * float(dados['Altura'])) - (6.8 * int(dados['Idade']))
    else:
        valor = 655 + (4.3 * float(dados['Peso'])) + (4.7 * float(dados['Altura'])) - (4.7 * int(dados['Idade']))
    print('%.3f' % valor)


metabolismo(dados)
