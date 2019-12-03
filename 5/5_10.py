import random as r

def monte_carlo():
    odd = 0
    num = int(input('Digite o numero de jogadas: '))
    for i in range(num):
        x = r.uniform(0,2)
        y = r.uniform(0,2)
        if (x>0 and x<1 and y>1 and y<2):
            #print('Acertou no 1')
            odd+= 1
        elif (x>1 and y<x):
            #print('Acertou no 3')
            odd+=1

    percent = (odd / num) *100
    print('A percentagem de calhar numa zona ímpar foi: %.3f' %percent)

monte_carlo()