import turtle

turtle.speed(-1)
angle = 30
turtle.penup()
turtle.lt(90)
turtle.fd(100)
turtle.pendown()

def pointer ():
    turtle.fd(20)
    turtle.penup()
    turtle.fd(20)
    turtle.stamp()
    
def prep_next():
    turtle.penup()
    turtle.bk(140)
    turtle.rt(angle)
    turtle.fd(100)
    turtle.pendown()
    
for i in range(12):
    pointer()
    prep_next()
    
turtle.ht()
turtle.getscreen()._root.mainloop()