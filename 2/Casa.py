import turtle

def retangulo(x, y, lado, comp, orient1):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(orient1)
    for i in range(2):
        turtle.rt(90)
        turtle.fd(lado)
        turtle.rt(90)
        turtle.fd(comp)

def triangulo(x, y, lado, orient2):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(orient2)
    for a in range(3):
        turtle.fd(lado)
        turtle.lt(120)


#House Body
turtle.fillcolor('red')
turtle.begin_fill()
retangulo(0,0,100,100,0)
turtle.end_fill()

#House Chimney
turtle.fillcolor('black')
turtle.begin_fill()
retangulo(-15,80,80,20,0)
turtle.end_fill()

#House Roof
turtle.fillcolor('green')
turtle.begin_fill()
triangulo(-100,0,100,0)
turtle.end_fill()

turtle.getscreen()._root.mainloop()



        
    