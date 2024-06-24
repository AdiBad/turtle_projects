# imports
import turtle
from random import random
import winsound

# setup screen object
screen = turtle.Screen()
screen.setup(600, 450)
screen.bgcolor("#A67A5B")
screen.title("Circles make sound")

# place 2 circles on screen
turtles=[]
for i in range(2):
    t=turtle.Turtle(shape="circle")
    t.penup()
    t.goto(50,50)
    t.pendown()
    t.color("white")
    t.speed(0)
    turtles.append(t)

# move the circles
for i in range(100):
    steps = random()*100
    angle = 90
    [t.right(pow(-1, id)*angle) for id, t in enumerate(turtles)]
    [t.fd(steps) for t in turtles]
    x,y = t.pos()
    print(x, y)
    if abs(x)>200 and abs(x)<300:
        winsound.PlaySound('small-bell-ringing-02.wav', 0) 
        screen.bye()

screen.mainloop()

