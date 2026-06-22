from turtle import *
from time import *
from random import *
#SETUP
# screen
width=600
height=400
sc=Screen()
sc.bgcolor("white")
sc.title("Pong")
sc.setup(width,height)
sc.tracer(0, 0) #WICHTIG

#paddles
p_length=100 
p_width=20 
#1.1: Paddles hinzufügen
#vllt ein Paddle schon vorgeben zur Orientierung?

#ball
#1.2: Ball hinzufügen
#2.1: Variablen zur Bewegung hinzufügen

#Spielstand

#1.3: Spielstand hinzufügen

#HELPERFUNCTIONS (v.a. Tastensteurung)
def changeDirection():
    #3.1: Richtungsänderung des Balls implementieren
    #wird aufgerufen wenn der Ball mit einer Wand oder einem Paddle kollidiert#
    return

#2.2: Die Bewegungen der beiden Paddles implementieren
#3.1: Grenzen des Spielfelds bei der Bewegung des Paddles beachten
def paddle1up():
    #2.2
    #3.1
    return
def paddle1down():
    #2.2
    #3.1
    return
def paddle2up():
    #2.2
    #3.1
    return
    
def paddle2down():
    #2.2
    #3.1
    return

#Tastensteuerung   
def KeyTrue(x):
    keys[x]=True
def KeyFalse(x):
    keys[x]=False

keys=[False,False,False,False]
sc.listen()
sc.onkeypress(lambda: KeyTrue(0),"w")
sc.onkeypress(lambda: KeyTrue(1),"s")
sc.onkeypress(lambda: KeyTrue(2),"Up")
sc.onkeypress(lambda: KeyTrue(3),"Down")
sc.onkeyrelease(lambda: KeyFalse(0),"w")
sc.onkeyrelease(lambda: KeyFalse(1),"s")
sc.onkeyrelease(lambda: KeyFalse(2),"Up")
sc.onkeyrelease(lambda: KeyFalse(3),"Down")



#MAIN LOOP
changeDirection()
while True:
    sc.update()
    sleep(0.005)
    #2.2: Bewegung der Paddles
    #Eingaben abgfragen
    
    # 2.1: Ball bewegen

    #3.2: Treffer checken
    
    #3.1: Abprall vom Rand

    #3.3: Abprall von den Paddles
  
    #3,4: Spielende
