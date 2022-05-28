import turtle
import random
def city(start_XCOR,start_YCOR,end_XCOR,end_YCOR,color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start_XCOR,start_YCOR)
    turtle.pendown()
    turtle.goto(end_XCOR,end_YCOR)
def windows(start_XCOR,start_YCOR,color,fill_color):
    turtle.pencolor(color)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(start_XCOR,start_YCOR)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.pendown()
    for x in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
def stars(color):
    turtle.pencolor(color)
    number=10
    while number!=0:
        number-=1
        x=random.randint(-297,297)
        y=random.randint(248,290)
        if x>-297 and y>240:
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.dot()





