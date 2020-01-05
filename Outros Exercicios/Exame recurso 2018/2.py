import turtle as t

t.setworldcoordinates(-100, -100, 500, 500)


def small_line(comp):
    t.forward(comp)


def small_space(space):
    t.pu()
    t.fd(space)
    t.pd()


def linha(tamanho, small_size, space_size):
    flag = 1
    lado = 0
    while flag == 1:
        lado += small_size
        if lado >= tamanho:
            extra = lado - tamanho
            small_line(small_size - extra)
            break
        else:
            small_line(small_size)

        lado += space_size
        if lado >= tamanho:
            extra = lado - tamanho
            small_space(space_size - extra)
            break
        else:
            small_space(space_size)


def start(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def retangulo(comprimento, largura, small_line, espaco, x, y):
    start(x,y)
    for i in range(2):
        linha(comprimento, small_line, espaco)
        t.lt(90)
        linha(largura, small_line, espaco)
        t.lt(90)


def teste(comp, larg):
    for i in range(2):
        t.fd(comp)
        t.lt(90)
        t.fd(larg)
        t.lt(90)


comprimento = 300
largura = 200
x = 0
y = 0
tamanho = 15
espaco = 4

retangulo(comprimento, largura, tamanho, espaco, x, y)
teste(comprimento, largura)

t.hideturtle()
t.exitonclick()
