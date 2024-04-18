import pygame
import constants as C
import random
import math

def createParticle(quantity,oldCenter):
	for i in range(quantity):
		color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		size = 3.0#random.uniform(3.0, 5.0)
		particle = Particle(oldCenter, color, size)

class Particle(pygame.sprite.Sprite):
	"""Spawn Particle"""
	def __init__(self, oldCenter, color, size):
		super().__init__()
		self.color = color
		self.image = pygame.Surface([size, size])
		self.image.fill(color)
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter
		self.killTimer = 0

		C.all_sprites_list.add(self)
		C.particle_list.add(self)

		self.drawPos = pygame.Vector2(self.rect.center)

		#self.speed = random.randint(150,200)
		self.speed = 150
		self.rotation = random.randrange(0,360)
		self.moveX = round(self.speed * math.sin( math.radians(self.rotation) ))
		self.moveY = round(self.speed * math.cos( math.radians(self.rotation) ))

	def destroy(self):
		"""Destroy Particle"""
		self.kill()

	def move(self):
		"""Move Particle"""
		self.rect.x -= self.moveX * C.DT
		self.rect.y -= self.moveY * C.DT

	def update(self):
		self.move()

		self.killTimer += C.DT
		if self.killTimer >= 2:
			self.destroy()
