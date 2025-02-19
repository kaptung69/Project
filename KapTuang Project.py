import turtle
import random

screen = turtle.Screen()
screen.bgcolor('white')

tom = turtle.Turtle()
tom.speed(0)  
tom.color('grey')

step = 100
lth = 100
agl = 120

colorboxs = ['black','red','green','blue','pink']

def Trainangle(lth, agl, step):
    for i in range(step): 
        for b in range(2):
            tom.color(random.choice(colorboxs))
            tom.forward(lth + i * 2)  
            tom.right(agl + b)

