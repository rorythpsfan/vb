import pygame
import imageController as IC
import constants as C
import gameOver as GO
import soundManager
import projectiles

class Npc4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.cycle = IC.npc4Animation
		self.index = 0
		self.maxIndex = len(self.cycle)
		self.animationCounter = 0

		self.image = IC.npc4Animation[0]
		self.rect = self.image.get_rect()
		self.rect.x = 640
		self.rect.y = 0

		self.mask = pygame.mask.from_surface(self.image)


		C.all_sprites_list.add(self)
		C.npc_list.add(self)
#		C.player_sprite_list.add(self)


	def animate(self):

		self.maxIndex = (len(self.cycle)-1)
		if self.index > self.maxIndex:
			self.index = 0

		self.image = self.cycle[self.index]
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(self.cycle)-1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def draw(self, SCREEN, camera):
		pos = (self.rect.x - camera.position.x,self.rect.y - camera.position.y)

		C.SCREEN.blit(self.image, pos)

	def destroy(self):
		C.all_sprites_list.remove(self)
		C.npc_list.remove(self)
		self.kill()

	def update(self):


		self.animate()


		#Draw mask and rectangle for debug

	#	pygame.draw.rect(C.SCREEN, C.SWEETBLUE, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 2)

	#	olist = self.mask.outline()
	#	pygame.draw.lines(C.SCREEN,(200,150,150),1,olist)

		#olist = self.mask.outline()
		#pygame.draw.polygon(C.SCREEN,(200,150,150),olist,0)

