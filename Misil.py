import pygame
from pygame.locals import *
from pygame.sprite import Sprite

import random

class Misil(Sprite):
	"""docstring for Misil"""
	def __init__(self,sprites,misiles,(rectx,recty),direccion=True):
		Sprite.__init__(self)
		self.images= [pygame.image.load("datos/misil.png"),
					pygame.image.load("datos/misil2.png"),
					pygame.image.load("datos/misil3.png")]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.rect.x,self.rect.y = (rectx,recty)
		sprites.add(self)
		misiles.add(self)
		self.estado_saliendo = False
		self.distancia_a_recorrer = 20
		self.direccion = direccion

	def update(self):
		if self.direccion:
			self.salida_arriba()
		else:
			self.salida_abajo()

		if self.estado_saliendo:
			self.image = self.images[random.randint(1,2)]
			self.rect.x += 28
			if self.rect.x >= 800:
				self.kill()

	def salida_arriba(self):
		if self.estado_saliendo==False:	
			self.rect.y -= 3
			self.rect.x +=.8
			self.distancia_a_recorrer -=1
			if self.distancia_a_recorrer==0:
				self.estado_saliendo=True

	def salida_abajo(self):
		if self.estado_saliendo==False:	
			self.rect.y += 3
			self.rect.x +=1.2
			self.distancia_a_recorrer -=1
			if self.distancia_a_recorrer==0:
				self.estado_saliendo=True
