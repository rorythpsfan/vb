import pygame
import imageController as IC
import math
import constants as C
import soundManager

class SmallBullet(pygame.sprite.Sprite):
	"""Spawn Small Bullet"""
	def __init__(self, rotation, centerPoint):
		super().__init__()
		self.rotation = rotation
		self.centerPoint = centerPoint
		self.cycle = IC.projectileOneCycle
		self.index = 0
		self.image = pygame.transform.rotozoom(self.cycle[self.index],self.rotation,1.0)
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.center = self.centerPoint
		self.animationCounter = 0
		self.speed = 50
	
		C.bullet_list.add(self)
		C.all_sprites_list.add(self)


	def animationCycle(self):
		"""Animate Small Bullet"""
		self.image = pygame.transform.rotozoom(self.cycle[self.index],self.rotation,1.0)
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(IC.projectileOneCycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def move(self):
		self.rect.x += self.speed

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.bullet_list.remove(self)
		self.kill()

	def update(self):
		"""Update small bullet"""

		#self.recursiveWalls()
		self.animationCycle()
		self.move()
		if self.rect.x >= (C.SCREENWIDTH):
			self.destroy()

class SpitBall(pygame.sprite.Sprite):
	"""Spawn Spitball"""
	def __init__(self, centerPoint):
		super().__init__()
		self.centerPoint = centerPoint
		self.cycle = IC.spitballCycle
		self.index = 0
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.center = self.centerPoint
		self.animationCounter = 0
		self.speed = 50
	
		C.bullet_list.add(self)
		C.all_sprites_list.add(self)

	def animationCycle(self):
		"""Animate Small Bullet"""
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(self.cycle) - 1):
				self.index = 2
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def move(self):
		self.rect.x += self.speed

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.bullet_list.remove(self)
		self.kill()

	def update(self):
		"""Update spitball"""

		#self.recursiveWalls()
		self.animationCycle()
		self.move()
		if self.rect.x >= (C.SCREENWIDTH):
			self.destroy()

class Beam(pygame.sprite.Sprite):
	"""Spawn Small Bullet"""
	def __init__(self, rectX, rectY):
		super().__init__()
		self.index = 0
		self.image = IC.beamCycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = rectX
		self.rect.y = rectY
		self.animationCounter = 0
		self.speed = 0
		self.killTimer = 0
	
		C.beam_list.add(self)
		C.all_sprites_list.add(self)

	def animationCycle(self):
		self.image = IC.beamCycle[self.index]
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(IC.beamCycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.beam_list.remove(self)
		self.kill()

	def update(self):
		#self.recursiveWalls()
		self.animationCycle()
		self.killTimer += C.DT
		if self.killTimer >= 2:
			self.kill()

class SoundWave(pygame.sprite.Sprite):
	def __init__(self, rectX, rectY):
		super().__init__()
		self.index = 0
		self.cycle = IC.soundWaveCycle
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = rectX-18
		self.rect.y = rectY + 48
		self.animationCounter = 0
		self.speed = 30
	
		C.projectile_list.add(self)
		C.all_sprites_list.add(self)

	def animationCycle(self):
		self.image = self.cycle[self.index]
		self.animationCounter += C.DT
		if self.animationCounter >= .2:
			if self.index == (len(self.cycle) - 1):
				self.index = 5
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def move(self):
		self.rect.x -= self.speed

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.projectile_list.remove(self)
		self.kill()

	def update(self):
		#self.recursiveWalls()
		self.animationCycle()
		self.move()
		if self.rect.x <= (0 - self.rect.w):
			self.destroy()

class ToxicGas(pygame.sprite.Sprite):
	def __init__(self, rectX, rectY):
		super().__init__()
		self.index = 0
		self.cycle = IC.toxicGasCycle
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = rectX
		self.rect.y = rectY
		self.animationCounter = 0
		self.speed = 30
	
		C.projectile_list.add(self)
		C.all_sprites_list.add(self)

	def animationCycle(self):
		self.image = self.cycle[self.index]
		self.animationCounter += C.DT
		if self.animationCounter >= .2:
			if self.index == (len(self.cycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def move(self):
		self.rect.x -= self.speed

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.projectile_list.remove(self)
		self.kill()

	def update(self):
		#self.recursiveWalls()
		self.animationCycle()
		self.move()
		if self.rect.x <= (0 - self.rect.w):
			self.destroy()


