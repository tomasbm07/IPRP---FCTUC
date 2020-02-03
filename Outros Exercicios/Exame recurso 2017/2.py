import turtle as t
t.speed(0)


def poligno_triangulo(lados, dim):
    for i in range(lados):
        triangulo(dim)
        t.fd(dim)
        t.rt(360/lados)


def triangulo(dim):
    for i in range(3):
        t.fd(dim)
        t.lt(360/3)


lados = 6
size = 80
poligno_triangulo(lados, size)
t.exitonclick()
