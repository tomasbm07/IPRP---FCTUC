import turtle

t=turtle.Turtle()
angle=5
size=10

def square():
    for i in range(4):
        t.rt(90)
        t.fd(size)

def next():
    t.rt(7)
         
for a in range(30):
    square()
    next()
    #angle=angle-10
    size=size+7
    
turtle.getscreen()._root.mainloop()
    