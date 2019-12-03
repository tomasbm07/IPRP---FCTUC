import turtle
import random

t = turtle.Turtle()

for i in range(50):  
    t.forward(random.randint(1,120))
    t.pencolor(random.random(),random.random(),random.random())
    direction = random.randint(0,1)
    
    if direction==0:
        t.left(random.randint(1,360))
    else:
        t.right(random.randint(1,360))
        
turtle.getscreen()._root.mainloop()
    