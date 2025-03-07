import turtle

screen = turtle.Screen()
screen.bgcolor('white')

tom = turtle.Turtle()
tom.speed(0)
tom.color('black')

tom.pu()
tom.goto(0, 250)  # Move turtle to start position
tom.pd()

sizes = 250
decress = 8

for i in range(30):  # Adjusted number of circles for better alignment
    tom.circle(sizes)
    tom.pu()
    tom.rt(90)
    tom.fd(decress)
    tom.lt(90)
    tom.pd()
    sizes -= decress

tom.pu()
tom.goto(0, -250)
tom.pd()
tom.lt(90)
tom.fd(300)

tom.rt(150)
tom.fd(10)
tom.bk(10)
tom.lt(300)
tom.fd(10)
tom.bk(10)
tom.rt(150)
