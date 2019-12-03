import turtle
import random

turtle.speed(-5)

def quadrado(lado,comp):
    for i in range(2):
        turtle.fd(lado)
        turtle.rt(90)
        turtle.fd(comp)
        turtle.rt(90)
        
#Quadrado Principal
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
for a in range(4):
    turtle.fd(400)
    turtle.rt(90)
    
#Quadrados pequenos
xoao=180
for b in range(100):
    turtle.penup()
    turtle.setpos(random.uniform(-xoao,xoao),random.uniform(-xoao,xoao))
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    quadrado(random.randint(5,30),random.randint(5,30))
    turtle.end_fill()    

turtle.getscreen()._root.mainloop()