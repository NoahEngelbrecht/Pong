from turtle import Turtle, Screen


game = True
boll_hastighet_x = 5
boll_hastighet_y = 5

def flytta_upp():
    ny_plats = spelfigur1.ycor() + 20
    spelfigur1.goto(spelfigur1.xcor(), ny_plats)

def flytta_ner():
    ny_plats = spelfigur1.ycor() - 20
    spelfigur1.goto(spelfigur1.xcor(), ny_plats)

def flytta_upp2():
    ny_plats = spelfigur2.ycor() + 20
    spelfigur2.goto(spelfigur2.xcor(), ny_plats)

def flytta_ner2():
    ny_plats = spelfigur2.ycor() - 20
    spelfigur2.goto(spelfigur2.xcor(), ny_plats)

def flytta_bollen():
    global boll_hastighet_x, boll_hastighet_y
    boll_x = boll.xcor() + boll_hastighet_x
    boll_y = boll.ycor() + boll_hastighet_y
    boll.goto(boll_x, boll_y)

    if boll.ycor() > 290: 
        boll.sety(290)  
        boll_hastighet_y *= -1 

    elif boll.ycor() < -290: 
        boll.sety(-290) 
        boll_hastighet_y *= -1

    if boll.xcor() > 380:
        boll.hideturtle()
        boll.goto(0,0)
        boll.showturtle()
   
    elif boll.xcor() < -380:
        boll.hideturtle()
        boll.goto(0,0)
        boll.showturtle()

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(5, 1, 2)
spelfigur1.penup()
spelfigur1.color("black")
spelfigur1.setposition(380, 0)
spelfigur1.color("white")

spelfigur2 = Turtle()
spelfigur2.shape("square")
spelfigur2.shapesize(5, 1, 2)
spelfigur2.penup()
spelfigur2.color("black")
spelfigur2.setposition(-380, 0)
spelfigur2.color("white")

screen.listen()
screen.onkey(flytta_upp, "Up")
screen.onkey(flytta_ner, "Down")
screen.onkey(flytta_upp2, "w")
screen.onkey(flytta_ner2, "s")

boll = Turtle()
boll.shape("circle")
boll.color("white")
boll.penup()

while game:
    flytta_bollen()

screen.exitonclick()