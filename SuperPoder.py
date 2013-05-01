import pygame
from pygame.locals import *
from pygame.sprite import Sprite

import random

class SuperPoder(Sprite):
	"""docstring for SuperPoder"""
	def __init__(self,sprites,superpoder,rect):
		Sprite.__init__(self)
		self.imagenes = [pygame.image.load("datos/poder.png"),
						pygame.image.load("datos/poder2.png")]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.x = rect[0]+60
		self.rect.y = rect[1]-60
		sprites.add(self)
		superpoder.add(self)
		self.paso = 0
		self.retraso = 4

	def update(self):
		self.image = self.imagenes[self.paso]
		if self.retraso < 0:
			self.retraso = 4
			self.paso+=1
		if self.paso>1:
			self.kill()
		else:
			self.retraso-=1