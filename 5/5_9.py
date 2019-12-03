import random as r
total_pair = 0
throws = int(input('Digite o numero de vezes que o dado seja lançado: '))

for i in range(throws):
    num = r.randint(1, 6)
    print('{}. {}'.format(i+1, num))
    if ((num % 2) == 0):
        total_pair += 1
percent = total_pair / num
print('A percentagem de numeros pares é %.3f: ' %(percent*100))
