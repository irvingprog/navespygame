import pygame
from pygame.locals import *
from pygame.sprite import Sprite

import random

from Disparo import DisparoChus,DisparoMabz,DisparoSting	
from SuperPoder import SuperPoder	
from Misil import Misil

class Nave(Sprite):
	def __init__(self,sprites,disparos,misiles,superpoder):
		Sprite.__init__(self)

		#Grupos
		self.sprites = sprites
		self.disparos = disparos
		self.misiles = misiles
		self.superpoder = superpoder

		#Funciones al crear la nave
		self._reiniciar()

		#Atributos de la nave
		self.velocidad = None
		self.vidas = 4

	def _reiniciar(self):
		#Estados
		self.estado_inmune=False
		self.estado_disparando=False
		self.estado_misil = False
		self.estado_superpoder = False

		#Contadores
		self.contador_inmune = 300
		self.contador_disparando=10
		self.numero_disparos=1	
		self.contador_misil = 30
		self.numero_misiles = 0
		self.contador_superpoder = 100
		self.numero_superpoderes = 4

		self.contador_invisible = 0;

	def update(self):
		self.tecla = pygame.key.get_pressed()
		self.actualizar_contador_invisible()
		self.moverconteclado()
		self.inmune()
		self.disparar()
		self.disparar_superpoder()
		self.disparar_misiles()

	def puede_chocar(self):
		return self.contador_invisible<=0

	def set_invisible(self):
		self.contador_invisible = 300

	def actualizar_contador_invisible(self):
		if self.contador_invisible > 0:
			self.contador_invisible -= 3
			if self.contador_invisible > 120:
				self.image = self.imagenes[random.randint(0,1)]
		else:
			self.image = self.imagenes[0]

	#def generar_vidas(self,sprites):


	def agregar_disparo(self):
		if self.numero_disparos == 1:
			self.numero_disparos = 2;
		elif self.numero_disparos == 2:
			self.numero_disparos = 3
		elif self.numero_disparos >=3:
		    self.numero_disparos=3

	def agregar_misil(self):
		if self.numero_misiles == 0:
			self.numero_misiles = 1;
		elif self.numero_misiles >= 1:
			self.numero_misiles = 2

	def disparar(self):
		if self.estado_disparando:
			if self.contador_disparando > 0:
				self.contador_disparando-=10

		if self.contador_disparando<=0:
			self.estado_disparando=False

		if self.estado_disparando==False and self.contador_disparando<10:
			self.contador_disparando+=1

	def disparar_superpoder(self):
		#print self.numero_superpoderes
		if self.numero_superpoderes>=1:
			if self.tecla[K_s] and self.estado_superpoder==False and self.contador_superpoder>0:
				self.contador_superpoder -= 2.5
				self.nuevo_superpoder = SuperPoder(self.sprites,self.superpoder,(self.rect.x,self.rect.y))
				self.superpoder.add(self.nuevo_superpoder)
				#self.nuevo_superpoder.sonido.play()
			if self.contador_superpoder<=0:
				self.contador_superpoder=0
				self.numero_superpoderes-=1
				self.estado_superpoder=True
			if self.estado_superpoder:
				self.contador_superpoder+=.2
				if self.contador_superpoder>=100:
					self.contador_superpoder=100
					self.estado_superpoder = False

	def disparar_misiles(self):
		if self.tecla[K_m] and self.estado_misil==False and self.contador_misil==30:
			self.estado_misil=True
			if self.numero_misiles==1:	
				self.nuevo_misil = Misil(self.sprites,self.misiles,(self.rect.x,self.rect.y),True)
			elif self.numero_misiles==2:
				self.nuevo_misil = Misil(self.sprites,self.misiles,(self.rect.x,self.rect.y),True)
				self.nuevo_misil = Misil(self.sprites,self.misiles,(self.rect.x,self.rect.y),False)

		if self.estado_misil:
			if self.contador_misil > 0:
				self.contador_misil -= 3

		if self.contador_misil <=  0:
			self.estado_misil=False

		if self.estado_misil==False and self.contador_misil<30:
			self.contador_misil+=1

	def inmune(self):
		if self.tecla[K_i] and self.estado_inmune==False and self.contador_inmune==300:
			self.estado_inmune=True

		if self.estado_inmune:
			self.image = self.imagenes[random.randint(0,2)]
			if self.contador_inmune > 0:
				self.contador_inmune-=.5

		if self.contador_inmune==0:
			self.estado_inmune=False
			self.image = self.imagenes[0]

		if self.estado_inmune==False and self.contador_inmune<300:
			self.contador_inmune+=1

	def moverconteclado(self):	
		if self.tecla[K_LEFT]:
			self.rect.x -= self.velocidad
		elif self.tecla[K_RIGHT]:
			self.rect.x += self.velocidad

		if self.tecla[K_UP]:
			self.rect.y -= self.velocidad
		elif self.tecla[K_DOWN]:
			self.rect.y += self.velocidad

		if self.rect.x <= 0:
			self.rect.x = 0
		elif self.rect.x + self.rect.width >= 800:
			self.rect.x = 800 - self.rect.width
		if self.rect.y <= 120:
			self.rect.y = 120
		elif self.rect.y + self.rect.height >= 480:
			self.rect.y = 480 - self.rect.height

class NaveChus(Nave):
	"""docstring for NaveChus"""
	def __init__(self,sprites,disparos,misiles,superpoder):
		#super(NaveChus, self).__init__(self)	
		Nave.__init__(self,sprites,disparos,misiles,superpoder)
		self.imagenes = [pygame.image.load("datos/naves/chus/nave.png"),
						pygame.image.load("datos/naves/chus/nave_transparente.png"),	
						pygame.image.load("datos/naves/chus/inmune.png")]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 250
		self.velocidad=10	

	def disparar(self):
		Nave.disparar(self)
		if self.tecla[K_SPACE] and self.estado_disparando==False and self.contador_disparando==10:
			self.estado_disparando=True
			if self.numero_disparos==1:
				self.nueva_bala = DisparoChus(self.sprites,self.disparos,(self.rect.x+80,self.rect.y))
			elif self.numero_disparos==2:
				self.nueva_bala = DisparoChus(self.sprites,self.disparos,(self.rect.x+50,self.rect.y-40))
				self.nueva_bala = DisparoChus(self.sprites,self.disparos,(self.rect.x+50,self.rect.y+40))
			elif self.numero_disparos==3:
				self.nueva_bala = DisparoChus(self.sprites,self.disparos,(self.rect.x+50,self.rect.y-40))
				self.nueva_bala = DisparoChus(self.sprites,self.disparos,(self.rect.x+80,self.rect.y))
				self.nueva_bala = DisparoChus(self.sprites,self.disparos,(self.rect.x+50,self.rect.y+40))
			self.nueva_bala.sonido.play()


class NaveMabz(Nave):
	"""docstring for NaveMabz"""
	def __init__(self,sprites,disparos,misiles,superpoder):
		#super(NaveMabz, self).__init__(self)	
		Nave.__init__(self,sprites,disparos,misiles,superpoder)
		self.imagenes = [pygame.image.load("datos/naves/mabz/nave.png"),
						pygame.image.load("datos/naves/mabz/inmune.png")]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()	
		self.rect.x = 100
		self.rect.y = 250
		self.velocidad = 10

	def disparar(self):
		Nave.disparar(self)
		if self.tecla[K_SPACE] and self.estado_disparando==False and self.contador_disparando==10:
			self.estado_disparando=True
			if self.numero_disparos==1:
				self.nueva_bala = DisparoMabz(self.sprites,self.disparos,(self.rect.x+80,self.rect.y))
			elif self.numero_disparos==2:
				self.nueva_bala = DisparoMabz(self.sprites,self.disparos,(self.rect.x+50,self.rect.y-40))
				self.nueva_bala = DisparoMabz(self.sprites,self.disparos,(self.rect.x+50,self.rect.y+40))
			elif self.numero_disparos==3:
				self.nueva_bala = DisparoMabz(self.sprites,self.disparos,(self.rect.x+50,self.rect.y-40))
				self.nueva_bala = DisparoMabz(self.sprites,self.disparos,(self.rect.x+80,self.rect.y))
				self.nueva_bala = DisparoMabz(self.sprites,self.disparos,(self.rect.x+50,self.rect.y+40))
			self.nueva_bala.sonido.play()
		




