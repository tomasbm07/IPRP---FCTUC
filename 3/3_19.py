import turtle as t
import random as r

def setup():
    t.pensize(2)
    t.pencolor('red')
    t.speed(0)
    t.penup()
    t.goto(-300,300)
    t.pendown()
    for i in range(4):
        t.fd(600)
        t.rt(90)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.pensize(1)
    t.pencolor('black')
setup()

def turn():
    max_x = 280
    max_y = 280
    tx = t.xcor()
    ty = t.ycor()
    if ((tx > max_x) or (tx < -max_x)):
        t.goto(0,0)
    elif ((ty > max_y) or (ty < -max_y)):
        t.goto(0,0)

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
        turn()
    if move[i] == 't':
        t.bk(comp)
        turn()
    if move[i] == 'd':
        t.rt(rotation)
        turn()
    if move [i] == 'e':
        t.lt(rotation)
        turn()
t.exitonclick()