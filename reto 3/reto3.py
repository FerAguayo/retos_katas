"""
Reto 3
Realiza el siguiente ejercicio con Phython y la librería de pygame
-------------------------------------------------------------------
● Con la librería de pygame crear una vista que simule a una lluvia
-------------------------------------------------------------------
Características mínimas:
-------------------------------------------------------------------
● Los objetos deben verse caer como una lluvia de arriba para abajo

● El objeto debe ser rectangular

● Los colores son de libre elección

"""
import pygame as pg
import random as ra
from clases import Rectangulos

#Inicio de pygame
pg.init()
x_max=1280
y_max=720
pantalla = pg.display.set_mode((x_max,y_max)) #Resolución de pantalla
pg.display.set_caption("Lluvia") #Nombre en la barra de pantalla de pygame
clock = pg.time.Clock() #Para controlar los frames dentro de la aplicación
running = True

lista_rectangulos=[]
for i in range(1,101):
    lista_rectangulos.append(Rectangulos(ra.randint(0,1280),0,ra.randint(20,50)))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pantalla.fill((130,127,124))

    for i in range(0,100):
        lista_rectangulos[i].caer(y_max + 20)
        lista_rectangulos[i].dibujar(pantalla)

    pg.display.flip()

    clock.tick(60)