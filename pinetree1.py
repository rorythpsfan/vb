import pygame
import random
import imageController as IC
import constants as C

class PineTree1(pygame.sprite.Sprite):
	"""Butterfly Class"""
	def __init__(self):
		super().__init__()
		self.index = 0
		self.image = random.choice(IC.pineTree1)
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect.x = random.randint(0, 2400)
		self.rect.y = random.randint(0, 1600)
		self.animationCounter = random.uniform(0,.5)



        # Mask for pixel-perfect collisions
		self.mask = pygame.mask.from_surface(self.image)

        # Add to sprite list to update and draw in the main program
		C.all_sprites_list.add(self)


    # Draw enemy
	def animate(self):
		self.image = IC.pineTree1[self.index]
		self.animationCounter += C.DT
		if self.animationCounter >= 0.5:
			if self.index == (len(IC.pineTree1) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def draw(self, SCREEN, camera):
		pos = (self.rect.x - camera.position.x,self.rect.y - camera.position.y)

		C.SCREEN.blit(self.image, pos)





	def recursiveWalls(self):
		if self.rect.x > (C.SCREENWIDTH):
			self.rect.x = (0-self.width)
		elif self.rect.y > (C.SCREENHEIGHT):
			self.rect.y = (0-self.width)
		elif self.rect.x < (0-self.width):
			self.rect.x = C.SCREENWIDTH
		elif self.rect.y < (0-self.width):
			self.rect.y = C.SCREENHEIGHT



    # Kills enemy (unused currently)
	def destroy(self):
		"""Clean up after death"""
		self.kill()

	# Moves and Draws the player every frame. Automatic when using Classes
	def update(self):
		"""Update neon light"""

		self.animate()
		self.recursiveWalls()
