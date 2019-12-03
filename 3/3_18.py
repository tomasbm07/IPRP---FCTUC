import turtle as t
import random as r
t.speed(0)
move = ''
tamanho = int(input('Digite o tamanho do ADN da turtle: '))
for c in range(tamanho):
    b = r.randint(1, 4)
    if b == 1:
        move += 'f'
    elif b == 2:
        move += 't'
    elif b == 3:
        move += 'd'
    elif b == 4:
        move += 'e'
    print(move)

# Randomize do movimento
comp = r.randint(1, 90)
rotation = r.randint(1,360)

for i in range (len(move)):
    if move[i] == 'f':
        t.fd(comp)
    if move[i] == 't':
        t.bk(comp)
    if move[i] == 'd':
        t.rt(rotation)
    if move [i] == 'e':
        t.lt(rotation)
t.exitonclick()