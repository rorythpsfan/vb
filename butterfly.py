import pygame
import random
import imageController as IC
import constants as C

class Butterfly(pygame.sprite.Sprite):
	"""Butterfly Class"""
	def __init__(self):
		super().__init__()
		self.cycle = IC.butterflyAnimation
		self.index = 0
		self.animationCounter = 0
		self.image = IC.butterflyAnimation[0]
		self.rect = self.image.get_rect()
		#self.width = self.image.get_width()
		#self.height = self.image.get_height()
		self.rect.x = random.randint(0, 2400)
		self.rect.y = random.randint(0, 1600)
		self.speedX = random.randint(-100,100)
		self.speedY = random.randint(-100,100)

		self.changeDirectionCounter = random.uniform(0,1)
		self.stopCounter = 0
		self.stop = False
		self.killTimer = 0

		self.mask = pygame.mask.from_surface(self.image)

		C.all_sprites_list.add(self)
		C.butterfly_list.add(self)

	def animate(self):
		self.image = self.cycle[self.index]
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(self.cycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def draw(self, SCREEN, camera):
		pos = (self.rect.x - camera.position.x,self.rect.y - camera.position.y)
		C.SCREEN.blit(self.image, pos)

	def move(self):
		self.changeDirectionCounter += C.DT

		if self.changeDirectionCounter >= 2:
			self.stop = True
			self.speedX = 0
			self.speedY = 0
		if self.stop == True:
			self.stopCounter += C.DT
			if self.stopCounter >= 1:			
				self.speedX = random.randint(-100,100)
				self.speedY = random.randint(-100,100)
				self.stop = False
				self.stopCounter = 0
				self.changeDirectionCounter = 0

		self.rect.x += self.speedX * C.DT
		self.rect.y += self.speedY * C.DT

	def recursiveWalls(self):
		if self.rect.x > (2400):
			self.rect.x = (0-self.rect.w)
		elif self.rect.y > (1600):
			self.rect.y = (0-self.rect.w)
		elif self.rect.x < (0-self.rect.w):
			self.rect.x = 2400
		elif self.rect.y < (0-self.rect.w):
			self.rect.y = 1600

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.butterfly_list.remove(self)
		self.kill()

	def update(self):
		self.move()
		self.animate()
		self.recursiveWalls()
		self.killTimer += C.DT
		if self.killTimer >= 360:
			self.destroy()
