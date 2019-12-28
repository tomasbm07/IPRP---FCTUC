import turtle as t

t.setworldcoordinates(-100, -100, 500, 500)
t.speed(1)


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
            # flag = 0
            break
        else:
            small_line(small_size)

        lado += space_size
        if lado >= tamanho:
            extra = lado - tamanho
            small_space(space_size - extra)
            # flag = 0
            break
        else:
            small_space(space_size)


def retangulo(comprimento, largura, small_line, espaco):
    for i in range(2):
        linha(comprimento, small_line, espaco)
        t.lt(90)
        linha(largura, small_line, espaco)
        t.lt(90)


# Comprimento, Largura, tamanho do traçejado, espaço entre as linhas
retangulo(300, 200, 15, 4)

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.hideturtle()
t.exitonclick()
