import pygame as pg
import random as ra

class Rectangulos:
    def __init__(self,pos_x,pos_y,vy,color=(68,76,145),w=2,h=25):
        self.pos_x= pos_x #posicion en el eje x 
        self.pos_y= pos_y #posicion en el eje y
        self.vy = vy #velocidad en el eje x
        self.color= color
        self.w= w #ancho del objeto
        self.h= h #alto del objeto
    
    def caer(self,y_max):
        self.pos_y += self.vy #hace que baje la gota
        self.h -= 0.5 # hace que el alto de la gota se encoja poco a poco

        if self.pos_y >= y_max  or self.h <= 0: #Si el tamaño de gota llega a 0 o llega al final de la pantalla
            self.pos_y = -10 #Genera una gota nueva 10 píxeles por encima para que no se vea de golpe
            self.pos_x = ra.randint(0,1280) #Genera una nueva posicion aleatoria en el eje x 
            self.h = ra.randint(20, 50) #Le devuelve un tamaño para que no sea 0
            
    
    def dibujar(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y,self.w,self.h))