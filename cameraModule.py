import pygame
import constants as C

class Camera:
	def __init__(self, player):
		self.player = player
		self.rect = C.SCREEN.get_rect()
		self.area = pygame.Rect(0, 0, 2400, 1600)
		self.position = pygame.Rect((0, 0), self.rect.size)
		self.position.center = self.area.center
		self.center = pygame.Vector2(self.position.center)

	def move(self):

		self.position.center = self.player.center;

		# Stop camera from leaving area.
		if not self.area.contains(self.position):
			self.position.clamp_ip(self.area)
			self.center = self.position.center
