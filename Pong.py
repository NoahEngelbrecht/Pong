from turtle import Turtle, Screen
import random

game = True
boll_hastighet_x = random.randint(2, 4)
boll_hastighet_y = random.randint(2, 4)
boll2_hastighet_x = random.randint(2, 4)
boll2_hastighet_y = random.randint(2, 4)

score1 = 0
score2 = 0

score = Turtle()
score.penup()
score.hideturtle()
score.color("white")
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

def flytta_upp():
    ny_plats = spelfigur1.ycor() + 30
    spelfigur1.goto(spelfigur1.xcor(), ny_plats)

def flytta_ner():
    ny_plats = spelfigur1.ycor() - 30
    spelfigur1.goto(spelfigur1.xcor(), ny_plats)

def flytta_upp2():
    ny_plats = spelfigur2.ycor() + 30
    spelfigur2.goto(spelfigur2.xcor(), ny_plats)

def flytta_ner2():
    ny_plats = spelfigur2.ycor() - 30
    spelfigur2.goto(spelfigur2.xcor(), ny_plats)

def uppdatera_score():
    score.clear()
    score.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))

def flytta_bollen():
    global boll_hastighet_x, boll_hastighet_y, score1, score2, game
    boll_x = boll.xcor() + boll_hastighet_x
    boll_y = boll.ycor() + boll_hastighet_y
    boll.goto(boll_x, boll_y)

    if boll.ycor() > 290: 
        boll.sety(290)  
        boll_hastighet_y *= -1 

    elif boll.ycor() < -290: 
        boll.sety(-290) 
        boll_hastighet_y *= -1

    if (boll.xcor() > 370 and spelfigur1.ycor() - 50 < boll.ycor() < spelfigur1.ycor() + 50) or \
       (boll.xcor() < -370 and spelfigur2.ycor() - 50 < boll.ycor() < spelfigur2.ycor() + 50):
        boll_hastighet_x *= -1

    if boll.xcor() > 380:
        boll.hideturtle()
        boll.goto(0, 0)
        boll.showturtle()
        score2 += 1 
        uppdatera_score()

    elif boll.xcor() < -380:
        boll.hideturtle()
        boll.goto(0, 0)
        boll.showturtle()
        score1 += 1 
        uppdatera_score() 

    if score1 == 3 or score2 == 3:
        game = False

def flytta_boll2():
    global boll2_hastighet_x, boll2_hastighet_y, score1, score2, game
    boll2_x = boll2.xcor() + boll2_hastighet_x
    boll2_y = boll2.ycor() + boll2_hastighet_y
    boll2.goto(boll2_x, boll2_y)

    if boll2.ycor() > 290: 
        boll2.sety(290)  
        boll2_hastighet_y *= -1 

    elif boll2.ycor() < -290: 
        boll2.sety(-290) 
        boll2_hastighet_y *= -1

    if (boll2.xcor() > 370 and spelfigur1.ycor() - 50 < boll2.ycor() < spelfigur1.ycor() + 50) or \
       (boll2.xcor() < -370 and spelfigur2.ycor() - 50 < boll2.ycor() < spelfigur2.ycor() + 50):
        boll2_hastighet_x *= -1

    if boll2.xcor() > 380:
        boll2.hideturtle()
        boll2.goto(0, 0)
        boll2.showturtle()
        score2 += 1 
        uppdatera_score()

    elif boll2.xcor() < -380:
        boll2.hideturtle()
        boll2.goto(0, 0)
        boll2.showturtle()
        score1 += 1 
        uppdatera_score() 

    if score1 == 3 or score2 == 3:
        game = False

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(5, 1, 1)
spelfigur1.penup()
spelfigur1.color("black")
spelfigur1.setposition(380, 0)
spelfigur1.color("white")

spelfigur2 = Turtle()
spelfigur2.shape("square")
spelfigur2.shapesize(5, 1, 1)
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

boll2 = Turtle()
boll2.shape("circle")
boll2.color("white")
boll2.penup()

while game:
    flytta_bollen()
    flytta_boll2()

score.clear()
if score1 == 3:
    score.write("Player 2 wins!", align="center", font=("Courier", 24, "normal"))
elif score2 == 3:
    score.write("Player 1 wins!", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
