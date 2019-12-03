import turtle as t

comp = 100
larg = 20

t.speed(0)
t.penup()
t.goto(-comp,0)
t.pendown()

#comp = int(input('digite o comp = '))
#larg = int(input('digite a larg = '))
num = int(input('digite o tamanho do piano = '))

def branco(comp, larg):
    for i in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(comp)
        t.rt(90)

def preto(comp,larg):
    t.fillcolor('black')
    t.begin_fill()
    for i in range(2):
        t.fd(larg/2)
        t.rt(90)
        t.fd(comp/2)
        t.rt(90)
    t.end_fill()

def piano(num):
    for i in range(num):
        for i in range(3):
            branco(comp,larg)
            t.fd(larg)
            preto(comp, larg)
            branco(comp,larg)
        t.fd(larg)

piano(num)
t.exitonclick()