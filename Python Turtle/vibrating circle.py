import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("red")
a=0
b=0
t.speed=10
t.penup()
t.goto(1,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==211:
        break
        t.hideturtle

