import turtle as t

print('f - frente | t - tras | d - direita | e - esquerda')
move = input('Digite um codigo para o movimento da tarta: ')

a = 50
for i in range (len(move)):
    if move[i] == 'f':
        t.fd(a)
    if move[i] == 't':
        t.bw(a)
    if move[i] == 'd':
        t.rt(90)
    if move [i] == 'e':
        t.lt(90)

t.exitonclick()