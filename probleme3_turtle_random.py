import turtle
import random
def carre(t):

    turtle.forward(t)
    turtle.left(90)
    turtle.forward(t)
    turtle.left(90)
    turtle.forward(t)
    turtle.left(90)
    turtle.forward(t)
    turtle.left(90)
def triangle(t):
    
    turtle.forward(t)
    turtle.left(120)
    turtle.forward(t)
    turtle.left(120)
    turtle.forward(t)
    turtle.left(120)

def cercle(t):
    turtle.circle(t / 2)

def dessin():
    turtle.colormode(255)
    turtle.speed(5) 
    
    reponse = input("tapez un chiffre entre 0 et 9 : ")
    if not reponse.isdigit():
        print("Erreur : Il faut taper un chiffre !")
        return
    
    n = int(reponse)

    for i in range(n):
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        taille = random.randint(20, 150)        
        forme = random.randint(1, 3)
        if forme == 1:
            carre(taille)
        elif forme == 2:
            triangle(taille)
        else:
            cercle(taille)
    turtle.done()
dessin()