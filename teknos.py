from tkinter import CENTER
import turtle
import time
import random
import math

jatek = turtle.Turtle()

# ablak létrehozása, beallitasok
ablak = turtle.Screen()
ablak.setup(width=800, height=600)
ablak.bgcolor("black")
ablak.title("PONG")
ablak.tracer(0)

# bal oldali ütő
bal_uto = turtle.Turtle()
bal_uto.speed(0)
bal_uto.shape("square")
bal_uto.shapesize(stretch_wid=6, stretch_len=1)
bal_uto.color("blue")
bal_uto.penup()
bal_uto.goto(-350, 0)

# jobb oldali ütő
jobb_uto = turtle.Turtle()
jobb_uto.speed(0)
jobb_uto.shape("square")
jobb_uto.shapesize(stretch_wid=6, stretch_len=1)
jobb_uto.color("pink")
jobb_uto.penup()
jobb_uto.goto(350, 0)

#labda
labda = turtle.Turtle()
labda.speed(5)
labda.shape("circle")
labda.color("white")
labda.penup()
labda.goto(0,0)
szog = random.uniform(0, 4 * math.pi)
sebesseg = 3
labda_változásX = sebesseg * math.cos(szog)
labda_változásY = sebesseg * math.sin(szog)

#pontszam
jobb_pont = 0
bal_pont = 0
pontszám = turtle.Turtle()
pontszám.speed(0)
pontszám.color("white")
pontszám.penup()
pontszám.hideturtle()
pontszám.goto(0,260)
pontszám.write(f"Jobb: {jobb_pont} | Bal: {bal_pont}", align="center", font=("Curier",24,"normal"))

#mozgas

def bal_uto_fel():
    y = bal_uto.ycor()
    if y < 240:
        y += 70
        bal_uto.sety(y)

def bal_uto_le():
    y = bal_uto.ycor()
    if y >-240:
        y -= 70
        bal_uto.sety(y)

def jobb_uto_fel():
    y = jobb_uto.ycor()
    if y < 240:
        y += 70
    jobb_uto.sety(y)

def jobb_uto_le():
    y = jobb_uto.ycor()
    if y > -240:
        y -= 70
    jobb_uto.sety(y)

#gombok
ablak.onkeypress(bal_uto_fel, "w")
ablak.onkeypress(bal_uto_le, "s")
ablak.onkeypress(jobb_uto_fel, "Up")
ablak.onkeypress(jobb_uto_le, "Down")

ablak.listen()

while True:

    time.sleep(0.01)
    ablak.update()

    labda.setx(labda.xcor() + labda_változásX )
    labda.sety(labda.ycor()+ labda_változásY) 

    if labda.ycor() > 240:
        labda.sety(240)
        labda_változásY *= -1

    if labda.ycor() < -240:
        labda.sety(-240)
        labda_változásY *= -1

    if labda.xcor() > 388:
        labda.goto(0,0)
        szog = random.uniform(0, 2 * math.pi)
        labda_változásX = sebesseg * math.cos(szog)
        labda_változásY = sebesseg * math.sin(szog)
        bal_pont +=1
        pontszám.clear()
        pontszám.write(f"Jobb: {jobb_pont} | Bal: {bal_pont}", 
        align="center", font=("Curier",24,"normal"))

    if labda.xcor() < -388:
        labda.goto(0,0)
        szog = random.uniform(0, 2 * math.pi)
        labda_változásX = sebesseg * math.cos(szog)
        labda_változásY = sebesseg * math.sin(szog)
        jobb_pont +=1
        pontszám.clear()
        pontszám.write(f"Jobb: {jobb_pont} | Bal: {bal_pont}", 
        align="center", font=("Curier",24,"normal"))

    if jobb_uto.xcor()-20 < labda.xcor() < jobb_uto.xcor() and jobb_uto.ycor()-40 < labda.ycor() < jobb_uto.ycor()+40:
        labda.setx(jobb_uto.xcor()-20)
        labda_változásX *= -1
    
    if bal_uto.xcor()+20 > labda.xcor() > bal_uto.xcor() and bal_uto.ycor()-40 < labda.ycor() < bal_uto.ycor()+40:
        labda.setx(bal_uto.xcor()+20)
        labda_változásX *= -1




