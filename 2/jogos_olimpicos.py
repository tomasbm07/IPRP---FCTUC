import turtle

turtle.speed(-5)
rad=50
t=turtle.Turtle()
t.pensize(5)
def circle ():
    t.circle(rad)
    
def top_next ():
    t.penup()
    t.fd(2*rad + 10)
    t.pendown()

def bot_next():
    t.penup()
    t.backward(2*rad)
    t.right(2*rad)
    t.pendown()    
    
t.pencolor('blue')
circle()
top_next()
t.pencolor('black')
circle()
top_next()
t.pencolor('red')
circle()

t.penup()
t.goto(50,-50)
t.pendown()
t.pencolor('yellow')
circle()
top_next()
t.pencolor('green')
circle()


turtle.getscreen()._root.mainloop()



    