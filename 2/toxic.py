import turtle

def out_circles(orient):
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(1):
        turtle.fd(lado_quad-100)
        turtle.lt(90)
        turtle.circle(120,120)
        turtle.setheading(orient)
        
#Quadrado Inicial
lado_quad=300
turtle.penup()
turtle.goto(-(lado_quad/2),lado_quad)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
for a in range(4):
    turtle.fd(lado_quad)
    turtle.rt(90)
turtle.end_fill

#Outside part
out_circles(120)


turtle.getscreen()._root.mainloop()
