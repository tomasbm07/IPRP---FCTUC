import turtle as t
import random as r

def game_start(x,y):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.speed(0)

#linhas, colunas, tamanho dos quadrados
def grelha(linhas, colunas, tamanho):
    for i in range(linhas):
        for i in range(colunas):
            quadrado(tamanho)
            t.fd(tamanho)
        next(tamanho, colunas)

def quadrado(tamanho):
    for i in range(4):
        t.fd(tamanho)
        t.rt(90)

def next(tamanho, colunas):
    t.pu()
    t.bk(tamanho * colunas)
    t.rt(90)
    t.fd(tamanho)
    t.lt(90)
    t.pd()

def start(x,y,linhas, colunas, tamanho):
    x_start = r.randrange(x, x + tamanho * colunas, tamanho)
    y_start = r.randrange(y - tamanho * linhas, y, tamanho)
    t.pu()
    t.goto(x_start, y_start)
    t.pd()
    t.shape('circle')
    t.shapesize(0.4)
    t.stamp()
    t.shape('classic')
    t.shapesize(1)

def movimento(x, y, linhas, colunas, tamanho, movimentos):
    t.pensize(2)
    for i in range(movimentos):
        orientation = check(x, y, linhas, colunas, tamanho)  # 1-cima 2-esquerda 3-baixo 4-direita
        if orientation == 1:
            t.seth(90)
            t.fd(tamanho)
        if orientation == 2:
            t.seth(180)
            t.fd(tamanho)
        if orientation == 3:
            t.seth(270)
            t.fd(tamanho)
        if orientation == 4:
            t.seth(0)
            t.fd(tamanho)

def check(x, y, linhas, colunas, tamanho):
    max_x = x + tamanho * colunas # (x, max_x) (-100, ) horizontal x maximo á direita
    min_y = y - tamanho * linhas # (y, max_y) (100, ) y maximo em baixo
    # x é min á esquerda
    # y é max em cima

    if (t.xcor() >= max_x): #nao passar do lado direito da grelha
        orientation = r.choice([1, 2, 3])

    elif(t.xcor() <= x): #nao passar do lado esquerdo da grelha
        orientation = r.choice([1, 3, 4])

    elif(t.ycor() >= min_y or t.ycor() >= abs(min_y)): #nao passar do lado de baixo da grelha
        orientation = r.choice([1, 2, 4])

    elif(t.ycor() >= y): #nao passar do lado de cima da grelha
        orientation = r.choice([2, 3, 4])

    else:
        orientation = r.choice([1, 2, 3, 4]) # 1-cima 2-esquerda 3-baixo 4-direita
    return orientation

def game(x, y, linhas, colunas, tamanho, movimentos):
    game_start(x, y)
    grelha(linhas, colunas, tamanho)
    start(x, y, linhas, colunas, tamanho)
    #t.speed(2)
    movimento(x, y, linhas, colunas, tamanho, movimentos)
    t.exitonclick()


#x, y, linhas, colunas, tamanho, nº de movimentos
game(-100, 100, 4, 4, 30, 30)
