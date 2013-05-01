import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class ArmaExtra(Sprite):
	"""docstring for ArmaExtra"""
	def __init__(self, sprites, x, y):
		Sprite.__init__(self,rect)
		self.image = pygame.image.load("datos/extra_extra.png")
		self.rect = self.image.get_rect()

	def update(self):
		pass	