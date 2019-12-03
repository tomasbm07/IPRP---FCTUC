import turtle
colors = ['red','purple','blue','green','orange','yellow']
t = turtle.Pen()
t.speed(-1)
turtle.bgcolor('black')
for x in range(500):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.fd(x)
    t.lt(59)
    print(x)
turtle.exitonclick()
