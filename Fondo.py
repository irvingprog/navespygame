import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Fondo(Sprite):
	"""docstring for Fondo"""
	def __init__(self,x):
		Sprite.__init__(self)
		self.image = pygame.image.load("datos/fondo.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = 0

	def update(self):
		self.movimiento()

	def movimiento(self):
		self.rect.x -= 3
		if self.rect.x <= -800:
			self.rect.x = 800

		
