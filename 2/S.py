import turtle as t

def semi_circ(rad):
    t.rt(90)
    t.circle(rad,180)
    
radius = (input('Digite o raio das circunferencias: '))
radius = int(radius)
#radius = 50semi_circ(radius)
t.rt(90)
t.penup()
semi_circ(radius)
t.pendown()
t.circle(radius,180)
t.exitonclick()