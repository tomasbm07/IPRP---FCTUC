import turtle as t

circulo = 200
t.penup()
t.goto(0,-circulo)
t.pendown()
t.speed(2)

def part1():
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.lt(90)
    t.circle(-circulo,180)
    t.circle(-circulo/2,180)
    t.circle(circulo/2,180)
    t.end_fill()

def small(x,y,color):
    t.penup()
    t.goto(x+20,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
part1()
t.pensize(2)
t.circle(circulo,180)
small(circulo/2,0,'white')
small(-(circulo/2),0,'black')
t.ht()

t.exitonclick()