import turtle as t

def star (size,pen_size):
    for i in range(30):
        t.forward(size)
        t.right(144)
        size = size + 6*i
        pen_size = pen_size + 1
        t.pensize(pen_size)
t.fillcolor('blue')
t.speed(-5)
t.begin_fill()
for a in range(1):
    star(200,2)
t.end_fill()
t.exitonclick()