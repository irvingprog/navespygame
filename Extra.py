import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import random

class Extra(Sprite):
	"""docstring for Extra"""
	def __init__(self,sprites):
		Sprite.__init__(self)

	def update(self):
		self.movimiento_de_extra()

	def movimiento_de_extra(self):
		pass

class ExtraDisparo(Extra):
	"""docstring for ClassName"""
	def __init__(self):
		super(ExtraDisparo, self).__init__(self)
		self.image = pygame.image.load("datos/extradisparo.png")
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(20,500)
		self.rect.y = random.randint(-150,-20)

	def movimiento_de_extra(self):
		self.rect.x += 3
		self.rect.y += 8
		if self.rect.y > 600:
			self.kill()

class ExtraMisil(Extra):
	"""docstring for ExtraMisil"""
	def __init__(self):
		super(ExtraMisil, self).__init__(self)
		self.image = pygame.image.load("datos/extramisil.png")
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(400,750)
		self.rect.y = random.randint(750,770)

	def movimiento_de_extra(self):
		self.rect.x -= 3
		self.rect.y -= 8
		if self.rect.y+self.rect.width < 0:
			self.kill()

class ExtraArmaExtra(Extra):
	"""docstring for ExtraArmaExtra"""
	def __init__(self):
		super(ExtraArmaExtra, self).__init__(self)
		self.image = pygame.image.load("datos/extra_extra.png")
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(10,400)
		self.rect.y = random.randint(750,770)

	def movimiento_de_extra(self):
		self.rect.x += 3
		self.rect.y -= 8
		if self.rect.y+self.rect.width < 0:
			self.kill()	


