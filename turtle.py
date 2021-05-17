import turtle

import random

import math

 

player=turtle.Turtle()

player.color('blue')

player.shape('turtle')

player.penup()

player.speed(0)

screen=player.getscreen()

 

a1= turtle.Turtle()

a1.color("red")

a1.shape("circle")

a1.penup()

a1.speed(0)

a1.goto(random.randint(-400, -400), random.randint(-300, 300))

 

a2= turtle.Turtle()

a2.color("red")

a2.shape("circle")

a2.penup()

a2.speed(0)

a2.goto(random.randint(-400, -400), random.randint(-300, 300))

 

a3= turtle.Turtle()

a3.color("red")

a3.shape("circle")

a3.penup()

a3.speed(0)

a3.goto(random.randint(-400, -400), random.randint(-300, 300))

 

def turnleft():

    player.left(30)

 

def turnright():

    player.right(30)

 

screen.onkeypress(turnleft, 'Left')

screen.onkeypress(turnright, 'Right')

screen.listen()

 

scoreturtle=turtle.Turtle()

scoreturtle.up()

scoreturtle.goto(300,300)

 

 

score=0

 

def play():

    player.fd(2)

    a1.fd(10)

    a2.fd(12)

    a3.fd(15)

    a1x,a1y=a1.pos()

    if a1x > 400:

        a1.goto(random.randint(-400, -400), random.randint(-300, 300))

 

    a2x,a2y=a2.pos()

    if a2x > 400:

        a2.goto(random.randint(-400, -400), random.randint(-300, 300))

 

    a3x,a3y=a3.pos()

    if a3x > 400:

        a3.goto(random.randint(-400, -400), random.randint(-300, 300))

    global score

    score+=1

    scoreturtle.clear()

    scoreturtle.write(str(score)+'점')

    screen.ontimer(play,10)

 

screen.ontimer(play,10)
