import pygame
import constants as C
import butterfly as bf
import firefly as ff
import random

class Fade(pygame.sprite.Sprite):
	def __init__(self, player):
		super().__init__()
		self.rect = pygame.display.get_surface().get_rect()
		self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
		self.alpha = 120
	
		self.clocky = 0
		self.clocky2 = 0	
		self.gameHour = 18
		self.gameMinute = 0

		self.speed = 1#.1
		self.bugTimer = 0
		self.player = player
		C.fade_list.add(self)

		#print ("FADING")

	def draw(self):
		self.image.fill((0, 0, 0, self.alpha))
		C.SCREEN.blit(self.image, (0,0))	

	def update(self):
		self.draw()

		self.clocky += C.DT
		self.clocky2 += C.DT

		if self.clocky >= 60:
			self.gameHour += 1
			self.alpha += 20 * self.speed
			if self.alpha == 240: 
				self.speed *= -1
				#print("nighttime")

			elif self.alpha == 0:
				self.speed *= -1
				#print("daytime")


			self.clocky = 0

		if self.clocky2 >= 10:
			self.gameMinute += 10



			self.clocky2 = 0

			if self.gameHour >= 6 and self.gameHour < 12:
				C.LEVEL.butterfly = bf.Butterfly()
				C.LEVEL.butterfly = bf.Butterfly()

			if self.gameHour >= 18 and self.gameHour < 24:
				C.LEVEL.particle = ff.Particle([random.randint(0, 2400), random.randint(0, 1600)], random.uniform(-50, 50), random.uniform(-50, 50), "multiblue")
				C.LEVEL.particle = ff.Particle([random.randint(0, 2400), random.randint(0, 1600)], random.uniform(-50, 50), random.uniform(-50, 50), "multiblue")
				C.LEVEL.particle = ff.Particle([random.randint(0, 2400), random.randint(0, 1600)], random.uniform(-50, 50), random.uniform(-50, 50), "multiblue")
				C.LEVEL.particle = ff.Particle([random.randint(0, 2400), random.randint(0, 1600)], random.uniform(-50, 50), random.uniform(-50, 50), "multiblue")


		if self.gameHour >= 24:
			self.gameHour = 0

		if self.gameMinute >= 60:
			self.gameMinute = 0
			
		#print (str(self.gameHour)+":"+str(self.gameMinute))
		#print ("Number of butterflies: "+ (str(len(C.butterfly_list))))
		#print ("Number of fireflies: "+ (str(len(C.firefly_list))))
			
