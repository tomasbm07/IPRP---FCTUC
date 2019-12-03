import turtle

t = turtle.Turtle()
size = 150
d=13

for i in range(4):
    t.fd(size)
    t.lt(90)
print(size,d)
def prep_next():
    t.penup()
    t.fd(d)
    t.left(90)
    t.fd(d)
    t.pendown()
    d = d - 4
    size = int(150 - d*2)
    
prep_next()
#size= int(size-d)

for i in range(4):
    t.fd(size)
    t.rt(90)
    
print(size,d)
prep_next()

for i in range(4):
    t.fd(size)
    t.lt(90)

    
turtle.getscreen()._root.mainloop()
    
    
    