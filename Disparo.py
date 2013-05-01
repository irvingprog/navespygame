import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Disparo(Sprite):
	"""docstring for Disparo"""
	def __init__(self, sprites, disparos, (x, y)):
		Sprite.__init__(self)
		self.sonido = pygame.mixer.Sound("datos/musica/disparo.wav")
		sprites.add(self)
		disparos.add(self)
		self.velocidad = None

	def update(self):
		self.movimientodisparo()

	def movimientodisparo(self):
		self.rect.x += self.velocidad
		if self.rect.x >= 800:
			self.kill()

class DisparoChus(Disparo):
	"""docstring for DisparoChus"""
	def __init__(self, sprites, disparos, (x, y)):
		Disparo.__init__(self, sprites, disparos, (x, y))
		self.image = pygame.image.load("datos/naves/chus/fuego.png")
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = (x, y)
		self.velocidad = 25


class DisparoMabz(Disparo):
	"""docstring for DisparoMabz"""
	def __init__(self, sprites, disparos, (x, y)):
		Disparo.__init__(self, sprites, disparos, (x, y))
		self.image = pygame.image.load("datos/naves/mabz/fuego.png")
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = (x, y)
		self.velocidad = 25
		
class DisparoSting(Disparo):
	"""docstring for DisparoSting"""
	def __init__(self, sprites, disparos, (x, y)):
		Disparo.__init__(self, sprites, disparos, (x, y))
		self.image = pygame.image.load("datos/naves/sting/fuego.png")
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = (x, y)
		self.velocidad = 18

class DisparoJefe(Disparo):
	"""docstring for DisparoJefe"""
	def __init__(self, sprites, disparos, (x, y)):
		Disparo.__init__(self, sprites, disparos, (x, y))
		self.image = pygame.image.load("datos/balajefe.png")
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = (x, y)
		self.velocidad = 12

	def movimientodisparo(self):
		self.rect.x -= self.velocidad
		if self.rect.x + self.rect.width <= 0:
			self.kill()
		