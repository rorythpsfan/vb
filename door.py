import pygame
import constants as C
import imageController as IC



class OpenDoor(pygame.sprite.Sprite):
	"""Door"""
	def __init__(self):
		super().__init__()
		self.index = 0
		self.timer = 0
		self.image = IC.doorAnimation[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		C.all_sprites_list.add(self)

	def update(self):
		self.image = IC.doorAnimation[self.index]
		self.timer += C.DT
		if self.timer >= .2:
			if self.index == (len(IC.doorAnimation)-1):
				self.index = 0
				self.kill()
			else:
				self.index += 1
				self.timer = 0


