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
            small_size = lado - tamanho
            small_line(small_size)
            flag = 0
        else:
            small_line(small_size)

        lado += space_size
        if lado >= tamanho:
            space_size = lado - tamanho
            small_space(space_size)
            flag = 0
        else:
            small_space(space_size)


def retangulo(comprimento, largura, small_line, espaco):
    for i in range(2):
        linha(comprimento, small_line, espaco)
        t.lt(90)
        linha(largura, small_line, espaco)
        t.lt(90)


# Comprimento, Largura, tamanho do traçejado, espaço entre as linhas
retangulo(200, 100, 5, 3)

for i in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(100)
    t.lt(90)

t.hideturtle()
t.exitonclick()
