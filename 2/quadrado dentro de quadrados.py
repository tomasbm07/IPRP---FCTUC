import turtle as t

size = 400
tamanho = size
t.speed(0)
t.penup()
t.goto(-(size/2),(size/2))
t.pendown()

def quadrado(lado):
    for i in range(4):
        t.fd(lado)
        t.rt(90)

def next_quad():
    t.penup()
    t.fd(20)
    t.rt(90)
    t.fd(20)
    t.lt(90)
    t.pendown()

for i in range(5):
    quadrado(tamanho)
    tamanho = tamanho - 40
    next_quad()
    quadrado(tamanho)
    tamanho = tamanho - 40
    next_quad()
    
t.exitonclick()
