import pygame
import imageController as IC
import constants as C
import gameOver as GO
import soundManager
import projectiles
import gameOver

class Player(pygame.sprite.Sprite):
	"""Player Class"""
	def __init__(self):
		super().__init__()
		self.cycle = IC.playerAnimation
		self.index = 0
		self.maxIndex = len(self.cycle)
		self.animationCounter = 0

		self.hudTimer = 0
		self.hudIndex = 0

		self.image = IC.playerAnimation[0]
		self.rect = self.image.get_rect()
		self.rect.x = ((C.SCREENWIDTH * .5) - (self.rect.w * .5))
		self.rect.y = ((C.SCREENHEIGHT * .5) - (self.rect.h * .5))
		self.speed = 400
		self.health = 100
		self.overload = 100
		self.threshold = 100
		self.gravity = 200
		self.score = 0
		self.pressedUp = False
		self.overloaded = False
		self.inFlyingLevel = False
		self.inOverheadLevel = False
		self.isInvincible = False
		self.isInvincibleCounter = 0
		self.resetRect = True
		self.direction = " "
		self.currentDirection = " "
		self.colliding = False
		self.lastX = self.rect.x
		self.lastY = self.rect.y

		self.currentNPC = 0

		self.inSocialMech = False

		self.mask = pygame.mask.from_surface(self.image)

		C.all_sprites_list.add(self)
		C.player_sprite_list.add(self)

	def move(self):

		if self.inFlyingLevel == False and self.inOverheadLevel == False:

			keys = pygame.key.get_pressed()

			if keys[pygame.K_RIGHT]:
				self.rect.x += self.speed * C.DT
				self.cycle = IC.playerWalkRight

			elif keys[pygame.K_LEFT]:
				self.rect.x -= self.speed * C.DT
				self.cycle = IC.playerWalkLeft

			else:
				self.cycle = IC.playerAnimation

			if keys[pygame.K_UP] and self.inFlyingLevel == False and self.inOverheadLevel == False:
				self.pressedUp = True
			else:
				self.pressedUp = False

		if self.inFlyingLevel == True:
			self.cycle = IC.playerFlying
			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP]:
				self.rect.y -= self.speed * C.DT
			if keys[pygame.K_DOWN]:
				self.rect.y += self.speed * C.DT
			if keys[pygame.K_LEFT]:
				self.rect.x -= self.speed * C.DT
			if keys[pygame.K_RIGHT]:
				self.rect.x += self.speed * C.DT

		if self.inOverheadLevel == True and self.inSocialMech == False:
			self.cycle = IC.playerAnimation
			self.speed = 200

			self.currentDirection = self.direction

			if self.colliding == False:
				keys = pygame.key.get_pressed()

				if keys[pygame.K_RIGHT]:
					self.direction = "right"
					self.rect.x += self.speed * C.DT
					self.cycle = IC.playerWalkRight

				elif keys[pygame.K_LEFT]:
					self.direction = "left"
					self.rect.x -= self.speed * C.DT
					self.cycle = IC.playerWalkLeft

				elif keys[pygame.K_UP]:
					self.direction = "up"
					self.rect.y -= self.speed * C.DT
					self.cycle = IC.playerWalkUp
				elif keys[pygame.K_DOWN]:
					self.direction = "down"
					self.rect.y += self.speed * C.DT
					self.cycle = IC.playerWalkDown

		if not self.inOverheadLevel:
			# Keep Player From Leaving Screen
			if self.rect.right >= C.SCREENWIDTH:
				self.rect.right = C.SCREENWIDTH
			if self.rect.left <= 0:
				self.rect.left = 0
			if self.rect.top <= 0:
				self.rect.top = 0
			if self.rect.bottom >= C.SCREENHEIGHT:
				self.rect.bottom = C.SCREENHEIGHT

		# Disable Gravity In Flying Level
		if not self.inFlyingLevel and not self.inOverheadLevel:
			# Gravity in normal levels
			if self.rect.bottom < C.SCREENHEIGHT:
				self.rect.y += self.gravity * C.DT

	def animate(self):

		# Draw overloaded
		if self.overloaded == True:
			self.cycle = IC.playerOverloaded

			# Use and decrement overload
			self.overload -= 0.5
			if self.overload <= 0:
				self.overloaded = False
		else:
			# Recharge Overload
			if self.overload < 100:
				self.overload += 0.5

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

	def shoot(self):
		"""Fire projectile"""
		pygame.mixer.Channel(2).play(soundManager.laser)
		centerPoint = self.rect.midright
		spitball = projectiles.SpitBall(centerPoint)

##############################################################################################################################
#######################Put this all in its own file to keep this file cleaner#################################################
##############################################################################################################################
	def drawHUD(self):

		font = pygame.font.Font(None, 70)
		score_colour = (0, 0, 0)

		# Define overload bar properties ################################
		overload_bar_x = 255  # X-coordinate of the left edge of the bar
		overload_bar_y = 60  # Y-coordinate of the top edge of the bar
		health_bar_x = 255
		health_bar_y = 10
		bar_width = 200  # Width of the empty bar
		bar_height = 30  # Height of the bar
		fill_color = (255, 0, 0)  # Color of the filled portion (red)
		empty_color = (0, 0, 0)   # Color of the unfilled portion (black)
		#################################################################
		C.SCREEN.blit(IC.hudAnimation[self.hudIndex], (0,0))
		self.hudTimer += C.DT
		if self.hudTimer >= .3:
			if self.hudIndex == (len(IC.hudAnimation)-1):
				self.hudIndex = 0
				self.hudTimer = 0
			else:
				self.hudIndex += 1
				self.hudTimer = 0	

		# Render and display the score
		score_text = str(self.score)  # Convert score to a string
		score_surface = font.render(score_text, True, score_colour)
		score_rect = score_surface.get_rect()
		score_rect.topleft = (145, 100)  # Adjust the position as needed

		# Blit (draw) the score onto the screen
		C.SCREEN.blit(score_surface, score_rect)
		# Calculate the width of the filled portion of the health bar based on player's health
		filled_width = int((self.health / 100) * bar_width)

		# Draw the empty portion of the health bar (red)
		pygame.draw.rect(C.SCREEN, (255, 0, 0), (health_bar_x, health_bar_y, bar_width, bar_height))

		# Draw the filled portion of the health bar (lime green)
		pygame.draw.rect(C.SCREEN, (50, 205, 50), (health_bar_x, health_bar_y, filled_width, bar_height))
	    
		# Calculate the width of the filled portion of the bar based on overload percentage
		filled_width = int((self.overload / self.threshold) * bar_width)
	    
		# Draw the empty portion of the overload bar (black)
		pygame.draw.rect(C.SCREEN, empty_color, (overload_bar_x, overload_bar_y, bar_width, bar_height))

		# Draw the filled portion of the overload bar (red)
		pygame.draw.rect(C.SCREEN, fill_color, (overload_bar_x, overload_bar_y, filled_width, bar_height))

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################	

	def destroy(self):
		self.kill()

	def update(self):

		if self.isInvincible == True:
			self.isInvincibleCounter += C.DT
			if self.isInvincibleCounter >= 1:
				self.isInvincible = False
				self.isInvincibleCounter = 0

		if self.health <= 0:
			C.GAMEOVER = True
			gameOver.show_game_over_screen()

		self.position = self.rect
		self.position.center = self.rect.center
		self.center = pygame.Vector2(self.position.center)

		self.animate()
		self.move()
		self.drawHUD()

		#print (self.rect.x)

		#Draw mask and rectangle for debug

	#	pygame.draw.rect(C.SCREEN, C.SWEETBLUE, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 2)

	#	olist = self.mask.outline()
	#	pygame.draw.lines(C.SCREEN,(200,150,150),1,olist)

		#olist = self.mask.outline()
		#pygame.draw.polygon(C.SCREEN,(200,150,150),olist,0)

