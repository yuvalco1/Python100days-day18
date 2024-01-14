import turtle

import colorgram
from random import randint, random, choice
from turtle import Turtle, Screen

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tim = Turtle()

    tim.speed(0)
    tim.shape("arrow")
    tim.color("blue")
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    for i in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    tim.clear()

    for i in range(3,11):
        tim.pencolor(random(), random(),random())
        angle = 360/i
        for j in range (1, i+1):
            tim.forward(100)
            tim.right(angle)

    tim.clear()
    tim.pensize(10)
    angles = [0,90,180,270]
    for i in range(20):
        tim.forward(30)
        tim.pencolor(random(), random(), random())
        tim.right(choice(angles))

    tim.clear()
    tim.pensize(1)
    for i in range (90):
        tim.circle(100)
        tim.right(4)
        tim.pencolor(random(), random(), random())

    colors = colorgram.extract("damien-hirst-spot-painting-for-sale.jpg",100)
    colors.pop(0)
    colors.pop(0)
    colors.pop(-1)
    turtle.colormode(255)
    tim.clear()
    tim.penup()
    tim.setpos(0,0)
    tim.pendown()
    tim.hideturtle()
    k=0
    for i in range(10):
        for j in range(10):
            tim.setpos(i * 40, j * 40)
            tim.pendown()
            tim.dot(20,colors[k % len(colors)-1].rgb)
            k += 1
            tim.penup()




    screen = Screen()
    screen.colormode(255)
    screen.exitonclick()