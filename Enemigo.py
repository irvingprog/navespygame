import pygame
from pygame.locals import *
from pygame.sprite import Sprite

import random

from Disparo import DisparoJefe

class Enemigo(Sprite):
	"""Clase base para todos los enemigos"""
	def __init__(self):
		Sprite.__init__(self)

	def update(self):
		self.movimientoenemigo()
		self.animacion()

	def animacion(self):
		self.image = self.images[random.randint(0,2)]

	def movimientoenemigo(self):
		if self.direccion == "recta":
			self.rect.x -= 4
			if self.rect.x + self.rect.width < 0:
				self.kill()
		elif self.direccion == "vertical_abajo":
			self.rect.y += 4
		elif self.direccion == "vertical_arriba":
			self.rect.y -= 4
		elif self.direccion == "diagonal_superior_izquierda":
			self.rect.x += 6
			self.rect.y += 8
		elif self.direccion == "diagonal_superior_derecha":
			self.rect.x -= 6
			self.rect.y += 8
		elif self.direccion == "diagonal_inferior_izquierda":
			self.rect.x +=6
			self.rect.y -=8
		elif self.direccion == "diagonal_inferior_derecha":
			self.rect.x -=6
			self.rect.y -=8

		#Eliminar objeto si se sale de pantalla
		if self.direccion == "vertical_abajo" or self.direccion == "diagonal_superior_derecha" or self.direccion == "diagonal_superior_izquierda":
			if self.rect.y > 600:
				self.kill()
		elif self.direccion == "vertical_arriba" or self.direccion == "diagonal_inferior_derecha" or self.direccion == "diagonal_inferior_izquierda":
			if self.rect.y + self.rect.height<0:
				self.kill()


class EnemigoRojo(Enemigo):
	"""docstring for Enemigo1"""
	def __init__(self,x,y,direccion="recta"):
		super(EnemigoRojo, self).__init__()
		self.images =[pygame.image.load("datos/enemigo1/enemigo1.png"),
						pygame.image.load("datos/enemigo1/enemigo2.png"),
						pygame.image.load("datos/enemigo1/enemigo3.png")]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.direccion = direccion

	def movimientoenemigo(self):
		Enemigo.movimientoenemigo(self)

class EnemigoAzul(Enemigo):
	"""docstring for EnemigoAzul"""
	def __init__(self, x, y, direccion="recta"):
		super(EnemigoAzul, self).__init__()
		self.images =[pygame.image.load("datos/enemigo2/enemigo1.png"),
						pygame.image.load("datos/enemigo2/enemigo2.png"),
						pygame.image.load("datos/enemigo2/enemigo3.png")]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.direccion = direccion

	def movimientoenemigo(self):
		Enemigo.movimientoenemigo(self)

class EnemigoJefe(Enemigo):
	"""docstring for EnmigoJefe"""
	def __init__(self, sprites, enemigos):
		super(EnemigoJefe, self).__init__()
		self.image = pygame.image.load("datos/jefe1.png")
		self.rect = self.image.get_rect()
		self.rect.x = 840
		self.rect.y = 250

		#Grupos
		self.sprites = sprites
		self.enemigos = enemigos

		self.abajo_movimiento = None

		self.vida = 1000

		self.fuente_vida = pygame.font.Font(None,18)

		#Contadores y estados
		self.estado_disparando = False
		self.contador_disparando = 40

	def disparar(self):
		if self.contador_disparando == 40:
			self.nueva_bala = DisparoJefe(self.sprites, self.enemigos, (self.rect.x-20,self.rect.y+40))
			self.estado_disparando=True		
		if self.estado_disparando:
			if self.contador_disparando > 0:
				self.contador_disparando-=1

		if self.contador_disparando<=0:
			self.estado_disparando=False

		if self.estado_disparando==False and self.contador_disparando<40:
			self.contador_disparando+=1

	def update(self):
		Enemigo.update(self)
		self.vida_surface = self.fuente_vida.render(str(self.vida)+"/1000",1,(255,255,255))
		self.disparar()

	def movimientoenemigo(self):
		if self.rect.x > 548 and self.rect.x <= 840:
			self.rect.x -=5
			if self.rect.x == 545:
				self.abajo_movimiento=True

		if self.abajo_movimiento:
			self.rect.y -= 8
			if self.rect.y <= 100:
				self.abajo_movimiento = False
		if self.abajo_movimiento == False:
			self.rect.y += 8
			if self.rect.y >=450:
				self.abajo_movimiento = True

	def animacion(self):
		pass
