import math as m

num = int(input('Digite um numero: '))
result = num % 2
if result == 0:
    print('O numero e par.')
    if ((num%4) == 0):
        print('O numero tambem e multiplo de 4.')
else:
    print('O numero e impar')