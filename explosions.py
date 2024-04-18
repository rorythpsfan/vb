import pygame
import imageController as IC
import soundManager
import constants as C



class ExplosionOne(pygame.sprite.Sprite):
	def __init__(self, oldCenter):
		super().__init__()
		self.index = 0
		self.image = IC.explosionOneCycle[self.index]	
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()

		self.rect.center = oldCenter

		self.timer = 0

		C.all_sprites_list.add(self)

	def animationCycle(self):
		self.timer += 1
		if self.timer % 8 == 0:
			if self.index == (len(IC.explosionOneCycle)-1):
				self.kill()
			else:
				self.index += 1
		self.image = IC.explosionOneCycle[self.index]

	def update(self):
		self.animationCycle()

class ExplosionTwo(pygame.sprite.Sprite):
	def __init__(self, oldCenter):
		super().__init__()
		self.index = 0
		self.image = IC.explosionTwoCycle[self.index]		
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()

		self.rect.center = oldCenter

		self.timer = 0

		C.all_sprites_list.add(self)

	def animationCycle(self):
		self.timer += 1
		if self.timer % 8 == 0:
			if self.index == (len(IC.explosionTwoCycle)-1):
				self.kill()
			else:
				self.index += 1
		self.image = IC.explosionTwoCycle[self.index]

	def update(self):
		self.animationCycle()

class ExplosionThree(pygame.sprite.Sprite):
	def __init__(self, oldCenter):
		super().__init__()
		self.index = 0
		self.image = IC.explosionThreeCycle[self.index]		
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()

		self.rect.center = oldCenter

		self.timer = 0

		C.all_sprites_list.add(self)

	def animationCycle(self):
		self.timer += 1
		if self.timer % 8 == 0:
			if self.index == (len(IC.explosionThreeCycle)-1):
				self.kill()
			else:
				self.index += 1
		self.image = IC.explosionThreeCycle[self.index]

	def update(self):
		self.animationCycle()

class Pow(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.index = 0
		self.cycle = IC.powAnimationCycle
		self.image = self.cycle[self.index]	
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()

		self.pos = pos
		self.rect.center = self.pos
		self.timer = 0

		C.all_sprites_list.add(self)
		C.explosion_list.add(self)

	def animationCycle(self):
		self.timer += C.DT
		if self.timer >= .1:
			if self.index == (len(self.cycle)-1):
				self.kill()
			else:
				self.index += 1
				self.timer = 0
		self.image = self.cycle[self.index]
		#pygame.draw.rect(C.SCREEN, C.BRIGHTPINK, [self.rect.x,self.rect.y, self.rect.w, self.rect.h], 2)

	def destroy(self):
		self.kill()

	def update(self):
		self.animationCycle()

class Boom(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.index = 0
		self.cycle = IC.boomAnimationCycle
		self.image = self.cycle[self.index]	
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()

		self.pos = pos
		self.rect.center = self.pos
		self.timer = 0

		C.all_sprites_list.add(self)
		C.explosion_list.add(self)

	def animationCycle(self):
		self.timer += C.DT
		if self.timer >= .1:
			if self.index == (len(self.cycle)-1):
				self.kill()
			else:
				self.index += 1
				self.timer = 0
		self.image = self.cycle[self.index]
		#pygame.draw.rect(C.SCREEN, C.BRIGHTPINK, [self.rect.x,self.rect.y, self.rect.w, self.rect.h], 2)

	def destroy(self):
		self.kill()

	def update(self):
		self.animationCycle()

class SpitSplosion(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.index = 0
		self.cycle = IC.spitsplosionCycle
		self.image = self.cycle[self.index]	
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()

		self.pos = pos
		self.rect.center = self.pos
		self.timer = 0

		C.all_sprites_list.add(self)
		C.explosion_list.add(self)

	def animationCycle(self):
		self.timer += C.DT
		if self.timer >= .05:
			if self.index == (len(self.cycle)-1):
				self.kill()
			else:
				self.index += 1
				self.timer = 0
		self.image = self.cycle[self.index]
		#pygame.draw.rect(C.SCREEN, C.BRIGHTPINK, [self.rect.x,self.rect.y, self.rect.w, self.rect.h], 2)

	def destroy(self):
		self.kill()

	def update(self):
		self.animationCycle()
