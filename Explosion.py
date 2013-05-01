import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Explosion(Sprite):
	"""docstring for Explosion"""
	def __init__(self,(x,y)):
		Sprite.__init__(self)
		self._cargar_imagenes()
		self.image = self.imagenes[0]
		self.sonido = pygame.mixer.Sound("datos/musica/explosion.wav")
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.paso = 0
		self.retraso = 4

	def _cargar_imagenes(self):
		self.imagenes = []
		for i in range(1,11):
			self.nueva_imagen = pygame.image.load("datos/explosion/"+str(i)+".png")
			self.imagenes.append(self.nueva_imagen)

	def update(self):
		self.image = self.imagenes[self.paso]
		if self.retraso <0:
			self.retraso = 4
			self.paso +=1
		if self.paso >9:
			self.kill()
		else:
			self.retraso-=1