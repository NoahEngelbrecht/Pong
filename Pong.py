from turtle import Turtle, Screen  # Importerar Turtle och Screen klasserna från turtle-modulen
import random  # Importerar random-modulen för att generera slumpmässiga värden

# Spelvariabler
game = True  # Spelstatus, True betyder att spelet pågår
boll_hastighet_x = random.randint(5, 10)  # Slumpar hastighet för bollen i x-led
boll_hastighet_y = random.randint(5, 10)  # Slumpar hastighet för bollen i y-led
boll2_hastighet_x = random.randint(5, 10)  # Slumpar hastighet för den andra bollen i x-led
boll2_hastighet_y = random.randint(5, 10)  # Slumpar hastighet för den andra bollen i y-led

# Lista med färger som kan användas för spelfigurer och bollar
colors = ("red", "blue", "green", "yellow", "orange", 
          "purple", "pink", "cyan", "magenta", "brown", 
          "white", "gray", "lightblue", "lightgreen")

# Poängvariabler för spelarna
score1 = 0  # Poäng för spelare 1
score2 = 0  # Poäng för spelare 2

# Skapar en turtle för att visa poängen
score = Turtle()
score.penup()  # Gör så att turtle inte ritar linjer när den rör sig
score.hideturtle()  # Döljer turtle-symbolen
score.color("white")  # Sätter färgen för texten till vit
score.goto(0, 260)  # Flyttar turtle till positionen (0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))  # Skriver ut startpoängen

# Funktion för att flytta spelare 1 uppåt
def flytta_upp():
    ny_plats = spelfigur1.ycor() + 30  # Beräknar ny y-position
    spelfigur1.goto(spelfigur1.xcor(), ny_plats)  # Flyttar spelaren till ny position

# Funktion för att flytta spelare 1 nedåt
def flytta_ner():
    ny_plats = spelfigur1.ycor() - 30  # Beräknar ny y-position
    spelfigur1.goto(spelfigur1.xcor(), ny_plats)  # Flyttar spelaren till ny position

# Funktion för att flytta spelare 2 uppåt
def flytta_upp2():
    ny_plats = spelfigur2.ycor() + 30  # Beräknar ny y-position
    spelfigur2.goto(spelfigur2.xcor(), ny_plats)  # Flyttar spelaren till ny position

# Funktion för att flytta spelare 2 nedåt
def flytta_ner2():
    ny_plats = spelfigur2.ycor() - 30  # Beräknar ny y-position
    spelfigur2.goto(spelfigur2.xcor(), ny_plats)  # Flyttar spelaren till ny position

# Funktion för att uppdatera poängen på skärmen
def uppdatera_score():
    score.clear()  # Rensar tidigare poäng
    score.write(f"Player 1: {score2}  Player 2: {score1}", align="center", font=("Courier", 24, "normal"))  # Skriver ut nya poäng

# Funktion för att flytta bollen
def flytta_bollen():
    global boll_hastighet_x, boll_hastighet_y, score1, score2, game  # Använd global variabler
    boll_x = boll.xcor() + boll_hastighet_x  # Beräknar ny x-position för bollen
    boll_y = boll.ycor() + boll_hastighet_y  # Beräknar ny y-position för bollen
    boll.goto(boll_x, boll_y)  # Flyttar bollen till ny position

    # Kollar om bollen träffar taket
    if boll.ycor() > 290: 
        boll.sety(290)  # Sätter bollen till takets y-position
        boll_hastighet_y *= -1  # Vänder bollen i y-led

    # Kollar om bollen träffar golvet
    elif boll.ycor() < -290: 
        boll.sety(-290)  # Sätter bollen till golvets y-position
        boll_hastighet_y *= -1  # Vänder bollen i y-led

    # Kollar om bollen träffar spelarna
    if (boll.xcor() > 355 and spelfigur1.ycor() - 50 < boll.ycor() < spelfigur1.ycor() + 50) or \
       (boll.xcor() < -355 and spelfigur2.ycor() - 50 < boll.ycor() < spelfigur2.ycor() + 50):
        boll_hastighet_x *= -1  # Vänder bollen i x-led

    # Kollar om bollen går utanför spelplanen till höger
    if boll.xcor() > 380:
        boll.hideturtle()  # Döljer bollen
        boll.goto(0, 0)  # Flyttar bollen till mitten
        boll.showturtle()  # Visar bollen igen
        score2 += 1  # Ökar poängen för spelare 2
        uppdatera_score()  # Uppdaterar poängen på skärmen

    # Kollar om bollen går utanför spelplanen till vänster
    elif boll.xcor() < -380:
        boll.hideturtle()  # Döljer bollen
        boll.goto(0, 0)  # Flyttar bollen till mitten
        boll.showturtle()  # Visar bollen igen
        score1 += 1  # Ökar poängen för spelare 1
        uppdatera_score()  # Uppdaterar poängen på skärmen

    # Kollar om någon spelare har nått 3 poäng
    if score1 == 3 or score2 == 3:
        game = False  # Avslutar spelet

# Funktion för att flytta den andra bollen
def flytta_boll2():
    global boll2_hastighet_x, boll2_hastighet_y, score1, score2, game  # Använd global variabler
    boll2_x = boll2.xcor() + boll2_hastighet_x  # Beräknar ny x-position för den andra bollen
    boll2_y = boll2.ycor() + boll2_hastighet_y  # Beräknar ny y-position för den andra bollen
    boll2.goto(boll2_x, boll2_y)  # Flyttar den andra bollen till ny position

    # Kollar om den andra bollen träffar taket
    if boll2.ycor() > 290: 
        boll2.sety(290)  # Sätter den andra bollen till takets y-position
        boll2_hastighet_y *= -1  # Vänder den andra bollen i y-led

    # Kollar om den andra bollen träffar golvet
    elif boll2.ycor() < -290: 
        boll2.sety(-290)  # Sätter den andra bollen till golvets y-position
        boll2_hastighet_y *= -1  # Vänder den andra bollen i y-led

    # Kollar om den andra bollen träffar spelarna
    if (boll2.xcor() > 355 and spelfigur1.ycor() - 50 < boll2.ycor() < spelfigur1.ycor() + 50) or \
       (boll2.xcor() < -355 and spelfigur2.ycor() - 50 < boll2.ycor() < spelfigur2.ycor() + 50):
        boll2_hastighet_x *= -1  # Vänder den andra bollen i x-led

    # Kollar om den andra bollen går utanför spelplanen till höger
    if boll2.xcor() > 380:
        boll2.hideturtle()  # Döljer den andra bollen
        boll2.goto(0, 0)  # Flyttar den andra bollen till mitten
        boll2.showturtle()  # Visar den andra bollen igen
        score2 += 1  # Ökar poängen för spelare 2
        uppdatera_score()  # Uppdaterar poängen på skärmen

    # Kollar om den andra bollen går utanför spelplanen till vänster
    elif boll2.xcor() < -380:
        boll2.hideturtle()  # Döljer den andra bollen
        boll2.goto(0, 0)  # Flyttar den andra bollen till mitten
        boll2.showturtle()  # Visar den andra bollen igen
        score1 += 1  # Ökar poängen för spelare 1
        uppdatera_score()  # Uppdaterar poängen på skärmen

    # Kollar om någon spelare har nått 3 poäng
    if score1 == 3 or score2 == 3:
        game = False  # Avslutar spelet

# Skapar spelplanen
screen = Screen()
screen.setup(800, 600)  # Sätter storleken på spelplanen
screen.bgcolor("black")  # Sätter bakgrundsfärgen till svart

# Skapar spelare 1
spelfigur1 = Turtle()
spelfigur1.shape("square")  # Sätter formen på spelaren till en kvadrat
spelfigur1.shapesize(5, 1, 1)  # Sätter storleken på spelaren
spelfigur1.penup()  # Gör så att turtle inte ritar linjer
spelfigur1.color("black")  # Sätter spelarfärgen till svart
spelfigur1.setposition(380, 0)  # Flyttar spelaren till positionen (380, 0)
spelfigur1.color(random.choice(colors))  # Sätter spelarfärgen till en slumpmässig färg från listan

# Skapar spelare 2
spelfigur2 = Turtle()
spelfigur2.shape("square")  # Sätter formen på spelaren till en kvadrat
spelfigur2.shapesize(5, 1, 1)  # Sätter storleken på spelaren
spelfigur2.penup()  # Gör så att turtle inte ritar linjer
spelfigur2.color("black")  # Sätter spelarfärgen till svart
spelfigur2.setposition(-380, 0)  # Flyttar spelaren till positionen (-380, 0)
spelfigur2.color(random.choice(colors))  # Sätter spelarfärgen till en slumpmässig färg från listan

# Lyssnar på tangenttryckningar för att styra spelarna
screen.listen()  # Aktiverar tangenttryckningar
screen.onkey(flytta_upp, "Up")  # Flyttar spelare 1 uppåt när "Up" trycks
screen.onkey(flytta_ner, "Down")  # Flyttar spelare 1 nedåt när "Down" trycks
screen.onkey(flytta_upp2, "w")  # Flyttar spelare 2 uppåt när "w" trycks
screen.onkey(flytta_ner2, "s")  # Flyttar spelare 2 nedåt när "s" trycks

# Skapar bollen
boll = Turtle()
boll.shape("circle")  # Sätter formen på bollen till en cirkel
boll.color(random.choice(colors))  # Sätter bollens färg till en slumpmässig färg från listan
boll.penup()  # Gör så att turtle inte ritar linjer

# Skapar den andra bollen
boll2 = Turtle()
boll2.shape("circle")  # Sätter formen på den andra bollen till en cirkel
boll2.color(random.choice(colors))  # Sätter den andra bollens färg till en slumpmässig färg från listan
boll2.penup()  # Gör så att turtle inte ritar linjer

# Huvudloopen för spelet
while game:
    flytta_bollen()  # Flyttar den första bollen
    flytta_boll2()  # Flyttar den andra bollen

# Rensar skärmen och visar vinnaren
score.clear()  # Rensar poängen på skärmen
if score1 == 3:
    score.write("Player 2 wins!", align="center", font=("Courier", 24, "normal"))  # Skriver ut att spelare 2 vinner
elif score2 == 3:
    score.write("Player 1 wins!", align="center", font=("Courier", 24, "normal"))  # Skriver ut att spelare 1 vinner

# Avsluta spelet (skärm stängs)
screen.mainloop()  # Håller fönstret öppet tills det stängs av användaren
