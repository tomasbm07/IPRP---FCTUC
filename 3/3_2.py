import math as m

def e3_2():
    a = int(input('Digite um lado do triangulo: '))
    b = int(input('Digite outro lado do triangulo: '))
    c = int(input('Digite o ultimo lado do triangulo: '))
    s = (a+b+c)/2
    area = m.sqrt(s*(s-a)*(s-b)*(s-c))
    print('A area do triangulo: ', area)

e3_2()