info = {'peso': 0, 'altura': 0}
info_keys = info.keys()
print(info)


def imc(info):
    valores = [(input('{}: '.format(x)))for x in info_keys]
    # print(valores)
    (info['peso']) = valores[0]
    info['altura'] = valores[1]
    imc = int(info['peso']) / (float(info['altura'])**2)
    info.update(imc=imc)
    print(info)
    print('%.2f' % imc)


imc(info)
