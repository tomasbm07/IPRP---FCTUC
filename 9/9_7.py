grau_total = int(input('Digite o grau máximo que pretende: '))
valor_grau = [int(input('Digite o valor associado á incógnita de grau {}: '.format(i))) for i in range(grau_total+1)]


def mostrar_polimomio():
    polinomio = ''
    for i in range(grau_total+1):
        if i == grau_total:
            a = '{}x^{}'.format(valor_grau[i], i)
        else:
            a = '{}x^{} + '.format(valor_grau[i], i)
        polinomio += a
        a.format(valor_grau[i], i)
    return polinomio


def horner(valores, x):
    if len(valores) == 1:
        return valores[0] + x
    if x == 0:
        return valores[0]
    return (valores[0] + x) * horner(valores[1:], x)


print(mostrar_polimomio())
# print(valor_grau)
x = int(input('Digite o valor de x que pretende calcular em f(x) = y: '))
print('y =', horner(valor_grau, x))
