#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

import random
from Timer import Timer

from Fondo import Fondo
from Enemigo import EnemigoRojo, EnemigoAzul, EnemigoJefe
from Nave import NaveChus, NaveMabz#, NaveSting
from Extra import ExtraDisparo,ExtraMisil,ExtraArmaExtra
from Explosion import Explosion

escena = None

SCREEN_WIDTH = 800;
SCREEN_HEIGHT = 600;

'''Creamos Pantala'''    
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       
pygame.display.set_caption("Aero TeamMex")
print "Creacion de ventana exitosa..."

'''
####################################################
#                  ESCENAS                         #
####################################################
'''

class Juego():
    def __init__(self):
        self.fondo1 = Fondo(0)
        self.fondo2 = Fondo(800) 

        self.fondo_pelicula = pygame.image.load("datos/fondopelicula.png")
        self.alerta = pygame.image.load("datos/alerta.png") 

        #Grupos
        self.sprites = pygame.sprite.Group()
        self.misiles = pygame.sprite.Group()
        self.disparos = pygame.sprite.Group()
        self.disparos_jefe = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.disparos_extra = pygame.sprite.Group()
        self.misiles_extra = pygame.sprite.Group()
        self.armaextra_extra = pygame.sprite.Group()
        self.superpoder = pygame.sprite.GroupSingle()
        self.nuevo_jefe_grupo = pygame.sprite.GroupSingle()

        self.nave = NaveChus(self.sprites,self.disparos,self.misiles,self.superpoder)
        self.sprites.add(self.nave)

        #Contadores creación de objetos
        self.contador_disparos_extra = 0
        self.contador_misiles_extra = 0
        self.contador_armaextra_extra = 0
        self.contador_enemigosrojos = 0
        self.contador_enemigosazules = 0

        self.vidas = 1
        self.puntos = 0

        self.fuente = pygame.font.Font(None,40)

        self.escudo_surface = self.fuente.render("Escudo ",1,(255,255,255))

        pygame.mixer.music.load("datos/musica/nivel1.wav")
        pygame.mixer.music.play(-1)

        self.nuevo_jefe = None

        #Creacion de temporizador
        self.temporizador = Timer()
        self.temporizador.start()

    def update(self):
        self.fondo1.update()
        self.fondo2.update()

    	for evento in pygame.event.get():
    		if evento.type == QUIT or evento.type == KEYDOWN and evento.key == K_ESCAPE:
    			exit()
        
        if self.temporizador.time() > 4: 
            #Creación de disparos extra
            self.contador_disparos_extra += 2
            if self.contador_disparos_extra >= 300:
                self.nuevo_disparoextra =ExtraDisparo()
                self.sprites.add(self.nuevo_disparoextra)
                self.disparos_extra.add(self.nuevo_disparoextra)
                self.contador_disparos_extra = 0

            #Creación de misiles extra
            self.contador_misiles_extra += 1
            if self.contador_misiles_extra >= 350:
                self.nuevo_misilextra = ExtraMisil()
                self.sprites.add(self.nuevo_misilextra)
                self.misiles_extra.add(self.nuevo_misilextra)
                self.contador_misiles_extra = 0

            #Creación de armas extras
            self.contador_armaextra_extra +=2
            if self.contador_armaextra_extra >= 320:
                self.nuevo_armaextra = ExtraArmaExtra()
                self.sprites.add(self.nuevo_armaextra)
                self.armaextra_extra.add(self.nuevo_armaextra)
                self.contador_armaextra_extra = 0

            if self.temporizador.time() < 60:
                #Creación de enemigos rojos
                self.contador_enemigosrojos +=4
                if self.contador_enemigosrojos >= 80:
                    self.nuevo_enemigorojo = EnemigoRojo(random.randint(500,1000),random.randint(-150,-20),"diagonal_superior_derecha")
                    self.sprites.add(self.nuevo_enemigorojo)
                    self.enemigos.add(self.nuevo_enemigorojo)
                    self.contador_enemigosrojos = 0

                #Creación de enemigos azules
                self.contador_enemigosazules +=4
                if self.contador_enemigosazules >= 80:
                    self.nuevo_enemigoazul = EnemigoAzul(random.randint(500,1000),random.randint(850,870),"diagonal_inferior_derecha")
                    self.sprites.add(self.nuevo_enemigoazul)
                    self.enemigos.add(self.nuevo_enemigoazul)
                    self.contador_enemigosazules = 0

        if self.temporizador.time() > 60 and self.temporizador.time() < 180:
            #Creación de enemigos rojos
            self.contador_enemigosrojos +=3
            if self.contador_enemigosrojos >= 80:
                self.nuevo_enemigorojo = EnemigoRojo(850,250,"recta")
                self.sprites.add(self.nuevo_enemigorojo)
                self.enemigos.add(self.nuevo_enemigorojo)
                self.contador_enemigosrojos = 0

            #Creación de enemigos azules
            self.contador_enemigosazules +=3
            if self.contador_enemigosazules >= 80:
                self.nuevo_enemigoazul = EnemigoAzul(850,300,"recta")
                self.sprites.add(self.nuevo_enemigoazul)
                self.enemigos.add(self.nuevo_enemigoazul)
                self.contador_enemigosazules = 0

        if self.temporizador.time() > 80 and self.temporizador.time() < 150:
            #Creación de enemigos rojos
            self.contador_enemigosrojos +=4
            if self.contador_enemigosrojos >= 80:
                self.nuevo_enemigorojo = EnemigoRojo(40,620,"diagonal_inferior_izquierda")
                self.sprites.add(self.nuevo_enemigorojo)
                self.enemigos.add(self.nuevo_enemigorojo)
                self.contador_enemigosrojos = 0

            #Creación de enemigos azules
            self.contador_enemigosazules +=4
            if self.contador_enemigosazules >= 80:
                self.nuevo_enemigoazul = EnemigoAzul(40,-20,"diagonal_superior_izquierda")
                self.sprites.add(self.nuevo_enemigoazul)
                self.enemigos.add(self.nuevo_enemigoazul)
                self.contador_enemigosazules = 0    

        if self.temporizador.time() > 180 and self.temporizador.time() < 250:
            #Creación de enemigos rojos
            self.contador_enemigosrojos +=4
            if self.contador_enemigosrojos >= 80:
                self.nuevo_enemigorojo = EnemigoRojo(400,-20,"vertical_abajo")
                self.sprites.add(self.nuevo_enemigorojo)
                self.enemigos.add(self.nuevo_enemigorojo)
                self.contador_enemigosrojos = 0

            #Creación de enemigos azules
            self.contador_enemigosazules +=4
            if self.contador_enemigosazules >= 80:
                self.nuevo_enemigoazul = EnemigoAzul(500,620,"vertical_arriba")
                self.sprites.add(self.nuevo_enemigoazul)
                self.enemigos.add(self.nuevo_enemigoazul)
                self.contador_enemigosazules = 0   

        if self.temporizador.time()>2 and self.nuevo_jefe==None:
            self.nuevo_jefe = EnemigoJefe(self.sprites, self.enemigos)
            self.sprites.add(self.nuevo_jefe)
            self.nuevo_jefe_grupo.add(self.nuevo_jefe)

        #Colisiones
        for colision in pygame.sprite.spritecollide(self.nave,self.disparos_extra,1):
            self.nave.agregar_disparo()

        for colision in pygame.sprite.spritecollide(self.nave,self.misiles_extra,1):
            self.nave.agregar_misil()

        for colision in pygame.sprite.spritecollide(self.nave,self.armaextra_extra,1):
            pass

        if self.nave.puede_chocar() and not self.nave.estado_inmune:
            for colision in pygame.sprite.spritecollide(self.nave,self.enemigos,1):
                (x,y) = colision.rect.center
                self.nueva_explosion = Explosion((x,y))
                self.sprites.add(self.nueva_explosion)
                self.nave.set_invisible()
            if self.nuevo_jefe:
                for colision in pygame.sprite.spritecollide(self.nave,self.nuevo_jefe_grupo,0):
                    self.nave.set_invisible()

        if self.nuevo_jefe!=None:
            for colision in pygame.sprite.spritecollide(self.nuevo_jefe,self.disparos,1):
                self.nuevo_jefe.vida -= random.randint(1,3)
                (x,y) = colision.rect.center
                self.nueva_explosion = Explosion((x,y))
                self.sprites.add(self.nueva_explosion)
                self.puntos+=random.randint(12,18) 

            for colision in pygame.sprite.spritecollide(self.nuevo_jefe,self.misiles,1):
                self.nuevo_jefe.vida -= random.randint(5,9)
                (x,y) = colision.rect.center
                self.nueva_explosion = Explosion((x,y))
                self.sprites.add(self.nueva_explosion)
                self.puntos+=random.randint(15,22)   

            for colision in pygame.sprite.spritecollide(self.nuevo_jefe,self.superpoder,1):
                self.nuevo_jefe.vida -= random.randint(2,4)
                self.puntos+=random.randint(13,17)    

        for colision in pygame.sprite.groupcollide(self.enemigos,self.superpoder,1,1):
            (x,y) = colision.rect.center
            self.nueva_explosion = Explosion((x,y))
            self.nueva_explosion.sonido.play()
            self.sprites.add(self.nueva_explosion)
            self.puntos+=random.randint(8,10)

        for colision in pygame.sprite.groupcollide(self.disparos,self.enemigos,1,1):
            (x,y) = colision.rect.center
            self.nueva_explosion = Explosion((x,y))
            self.nueva_explosion.sonido.play()
            self.sprites.add(self.nueva_explosion)
            self.puntos+=random.randint(8,10)

        for colision in pygame.sprite.groupcollide(self.misiles,self.enemigos,1,1):
            (x,y) = colision.rect.center
            self.nueva_explosion = Explosion((x,y))
            self.nueva_explosion.sonido.play()
            self.sprites.add(self.nueva_explosion)
            self.puntos+=random.randint(8,10)      

        self.vidas_surface = self.fuente.render("Vidas "+str(self.vidas),1,(255,255,255))
        self.puntos_surface = self.fuente.render("Puntos "+str(self.puntos),1,(255,255,255))

        self.sprites.update()

    def imprimir(self,screen):
        screen.blit(self.fondo1.image,self.fondo1.rect)
        screen.blit(self.fondo2.image,self.fondo2.rect)
        self.sprites.draw(screen)
        screen.blit(self.fondo_pelicula,(0,0))
        screen.blit(self.vidas_surface,(100,20))
        screen.blit(self.puntos_surface,(500,20))
        screen.blit(self.escudo_surface,(100,520))
        if self.nuevo_jefe!=None:
            screen.blit(self.nuevo_jefe.vida_surface,(self.nuevo_jefe.rect.x,self.nuevo_jefe.rect.y-20))     

    	pygame.display.flip()

class Menu():
    def __init__(self):
        pass

class Creditos():
    def __init__(self):
        pass

'''
####################################################
#              FUNCIONES                           #
#            CAMBIOS Y ESCENAS                     #
####################################################
'''

'''
####################################################
#              BUCLE PRINCIPAL                     #
####################################################
'''
def main():
    global escena
    pygame.init()
    
    '''Reloj'''
    reloj = pygame.time.Clock()
    
    escena=Juego()
        
    while True:
        escena.update()
        escena.imprimir(screen)
        print reloj.tick(60)
        
if __name__ == '__main__':
    main()
