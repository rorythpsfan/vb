import pygame
import imageController as IC
import constants as C
import random
import soundManager
import particle
import soundManager
import projectiles
import explosions

class NeonLight(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.cycle = IC.neonLight
		self.index = random.randint(0, len(self.cycle) - 1)
		self.animationCounter = random.uniform(0,.1)
		self.image = self.cycle[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(C.SCREENWIDTH, (C.SCREENWIDTH + 1000))
		self.rect.y = random.randrange(0, (C.SCREENHEIGHT - self.rect.h))
		self.speed = random.randint(100,400)
		self.rotation = 0
		self.shootTimer = random.uniform(0,5)
		self.beamActive = True
		self.hitPoints = 5
		self.explosionType = random.randint(0,2)

		# Mask for pixel-perfect collisions
		self.mask = pygame.mask.from_surface(self.image)

		# Add to sprite list to update and animate in the main program
		C.all_sprites_list.add(self)
		C.enemy_sprite_list.add(self)

	# animate enemy
	def animate(self):
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(self.cycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.index += 1
				self.animationCounter = 0

	def shoot(self):
		pygame.mixer.Channel(2).play(soundManager.laser)
		beam = projectiles.Beam(0, self.rect.y - 76)

	def move(self):
		# Move the enemy toward the player if the player is close

		self.rect.x -= self.speed * C.DT

		#Reset if off screen
		if self.rect.x <= 0 - self.rect.w:
			self.rect.x = random.randrange(C.SCREENWIDTH, (C.SCREENWIDTH + 1000))
			self.rect.y = random.randrange(0, (C.SCREENHEIGHT - self.rect.h))
			self.beamActive = True

	# Kills enemy (unused currently)
	def destroy(self):
		"""Clean up after death"""
		pygame.mixer.Channel(2).play(soundManager.explosion)
		if self.explosionType == 0:
			kerpow = explosions.Pow(self.rect.center)
		elif self.explosionType == 1:
			boom = explosions.Boom(self.rect.center)
		else:
			particleBlast = particle.createParticle(100, self.rect.center)

		C.all_sprites_list.remove(self)
		C.enemy_sprite_list.remove(self)
		C.NUMBEROFENEMIES -= 1
		self.kill()

	# Moves and animates the player every frame. Automatic when using Classes
	def update(self):
		"""Update neon light"""
		self.move()
		self.animate()
		if self.rect.x <= C.SCREENWIDTH - self.rect.w and self.beamActive == True:
			self.shoot()
			self.beamActive = False

		#pygame.draw.rect(C.SCREEN, C.BRIGHTPINK, [self.rect.x,self.rect.y, self.rect.w, self.rect.h], 2)

class BoomBox(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.cycle = IC.boomBox
		self.index = random.randint(0,len(self.cycle) - 1)
		self.animationCounter = random.uniform(0,.1)
		self.image = self.cycle[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(C.SCREENWIDTH, (C.SCREENWIDTH + 1000))
		self.rect.y = random.randrange(0, (C.SCREENHEIGHT - self.rect.h))
		self.speed = random.randint(100,400)
		self.hitPoints = 5
		self.explosionType = random.randint(0,2)

		# Mask for pixel-perfect collisions
		self.mask = pygame.mask.from_surface(self.image)

		# Add to sprite list to update and animate in the main program
		C.all_sprites_list.add(self)
		C.enemy_sprite_list.add(self)

		self.canShoot = True

	def shoot(self):
		pygame.mixer.Channel(2).play(soundManager.laser)
		soundwave = projectiles.SoundWave(self.rect.x, self.rect.y)

	# animate enemy
	def animate(self):
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(self.cycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.canShoot = True
				self.index += 1
				self.animationCounter = 0

	def move(self):
		# Move the enemy toward the player if the player is close

		self.rect.x -= self.speed * C.DT

		#Reset if off screen
		if self.rect.x <= 0 - self.rect.w:
			self.rect.x = random.randrange(C.SCREENWIDTH, (C.SCREENWIDTH + 1000))
			self.rect.y = random.randrange(0, (C.SCREENHEIGHT - self.rect.h))

	# Kills enemy (unused currently)
	def destroy(self):
		"""Clean up after death"""
		pygame.mixer.Channel(2).play(soundManager.explosion)
		if self.explosionType == 0:
			kerpow = explosions.Pow(self.rect.center)
		elif self.explosionType == 1:
			boom = explosions.Boom(self.rect.center)
		else:
			particleBlast = particle.createParticle(100, self.rect.center)
		C.all_sprites_list.remove(self)
		C.enemy_sprite_list.remove(self)
		C.NUMBEROFENEMIES -= 1
		self.kill()

	# Moves and animates the player every frame. Automatic when using Classes
	def update(self):
		"""Update boombox"""
		self.move()
		self.animate()
		if self.canShoot == True and self.index == 7 and self.rect.x < C.SCREENWIDTH - (self.rect.w * .5):

			self.shoot()
			self.canShoot = False

		#pygame.draw.rect(C.SCREEN, C.BRIGHTPINK, [self.rect.x,self.rect.y, self.rect.w, self.rect.h], 2)
        
class TrashCan(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.cycle = IC.trashCan
		self.index = random.randint(0,len(self.cycle) - 1)
		self.animationCounter = random.uniform(0,.1)
		self.image = self.cycle[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(C.SCREENWIDTH, (C.SCREENWIDTH + 1000))
		self.rect.y = random.randrange(0, (C.SCREENHEIGHT - self.rect.h))
		self.speed = random.randint(100,400)
		self.hitPoints = 5
		self.explosionType = random.randint(0,2)

		# Mask for pixel-perfect collisions
		self.mask = pygame.mask.from_surface(self.image)

		# Add to sprite list to update and animate in the main program
		C.all_sprites_list.add(self)
		C.enemy_sprite_list.add(self)

		self.canShoot = True

	def shoot(self):
		pygame.mixer.Channel(2).play(soundManager.laser)
		soundwave = projectiles.ToxicGas(self.rect.x, self.rect.y)

	# animate enemy
	def animate(self):
		self.image = self.cycle[self.index]
		self.mask = pygame.mask.from_surface(self.image)
		self.animationCounter += C.DT
		if self.animationCounter >= 0.1:
			if self.index == (len(self.cycle) - 1):
				self.index = 0
				self.animationCounter = 0
			else:
				self.canShoot = True
				self.index += 1
				self.animationCounter = 0

	def move(self):
		# Move the enemy toward the player if the player is close

		self.rect.x -= self.speed * C.DT

		#Reset if off screen
		if self.rect.x <= 0 - self.rect.w:
			self.rect.x = random.randrange(C.SCREENWIDTH, (C.SCREENWIDTH + 1000))
			self.rect.y = random.randrange(0, (C.SCREENHEIGHT - self.rect.h))

	# Kills enemy (unused currently)
	def destroy(self):
		"""Clean up after death"""
		pygame.mixer.Channel(2).play(soundManager.explosion)
		if self.explosionType == 0:
			kerpow = explosions.Pow(self.rect.center)
		elif self.explosionType == 1:
			boom = explosions.Boom(self.rect.center)
		else:
			particleBlast = particle.createParticle(100, self.rect.center)
		C.all_sprites_list.remove(self)
		C.enemy_sprite_list.remove(self)
		C.NUMBEROFENEMIES -= 1
		self.kill()

	# Moves and animates the player every frame. Automatic when using Classes
	def update(self):
		"""Update trashcan"""
		self.move()
		self.animate()

		if self.canShoot == True and self.index == 0 and self.rect.x < C.SCREENWIDTH - (self.rect.w * .5):

			self.shoot()
			self.canShoot = False

		#pygame.draw.rect(C.SCREEN, C.BRIGHTPINK, [self.rect.x,self.rect.y, self.rect.w, self.rect.h], 2)
