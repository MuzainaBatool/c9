import turtle
import random

listl=[50,60,70,80,90,100,110,120,130,140,150]
colors=['red','blue','green','pink','purple','grey','range']

def draw_things(l,c):
    for value in l:
        turtle.forward(value)
        turtle.pencolor(random.choice(c))
        (turtle.stamp())
        turtle.backward(value)
        turtle.right(30)
    
draw_things(listl,colors)
