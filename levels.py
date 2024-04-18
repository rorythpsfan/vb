import pygame
import random
import constants as C
import imageController as IC
import soundManager
import enemy
import door
import pytmx
import SVGEditor as SVG
import butterfly as bf
import firefly as ff
import npc1 as NPC1
import npc2 as NPC2
import npc3 as NPC3
import npc4 as NPC4
import npc5 as NPC5
import subprocess
import sys
IC.playerFlying = SVG.convert(target = None, cycleDirectory = IC.playerFlyingDirectory,  isMirrored = "no", scale = "small")

#Need SVGS / Non fixed size
#IC.boomAnimationCycle = SVG.convert(target = None, cycleDirectory = IC.boomAnimationCycleDirectory,  isMirrored = "no", scale = "small")
#IC.powAnimationCycle = SVG.convert(target = None, cycleDirectory = IC.powAnimationCycleDirectory,  isMirrored = "no", scale = "large")
#IC.soundWaveCycle = SVG.convert(target = None, cycleDirectory = IC.soundWaveCycleDirectory,  isMirrored = "no", scale = "small")
#IC.toxicGasCycle = SVG.convert(target = None, cycleDirectory = IC.toxicGasCycleDirectory,  isMirrored = "no", scale = "small")

#Off for now, Need SVGs
#####IC.beamCycle = SVG.convert(target = None, cycleDirectory = IC.beamCycleDirectory,  isMirrored = "no", scale = "small")
#####IC.neonLight = SVG.convert(target = None, cycleDirectory = IC.neonLightDirectory,  isMirrored = "no", scale = "small")
#####IC.boomBox = SVG.convert(target = None, cycleDirectory = IC.boomBoxDirectory,  isMirrored = "no", scale = "small")
#####IC.trashCan = SVG.convert(target = None, cycleDirectory = IC.trashCanDirectory,  isMirrored = "no", scale = "small")

IC.npc1Animation = SVG.convert(target = None, cycleDirectory = IC.npc1AnimationDirectory,  isMirrored = "yes", scale = "verysmall")
IC.npc2Animation = SVG.convert(target = None, cycleDirectory = IC.npc2AnimationDirectory,  isMirrored = "yes", scale = "verysmall")
IC.npc3Animation = SVG.convert(target = None, cycleDirectory = IC.npc3AnimationDirectory,  isMirrored = "yes", scale = "verysmall")
IC.npc4Animation = SVG.convert(target = None, cycleDirectory = IC.npc4AnimationDirectory,  isMirrored = "yes", scale = "verysmall")
IC.npc5Animation = SVG.convert(target = None, cycleDirectory = IC.npc5AnimationDirectory,  isMirrored = "yes", scale = "verysmall")
IC.butterflyAnimation = SVG.convert(target = None,  cycleDirectory = IC.butterflyAnimationDirectory,  isMirrored = "no", scale = "butterfly")

class Level0:
    def __init__(self, player):
    
        pygame.init()
        self.player = player
        self.player.cycle = IC.playerAnimation
        self.player.image = self.player.cycle[0]
        self.player.rect = self.player.image.get_rect()
        self.player.mask = pygame.mask.from_surface(self.player.image)
        self.cycle = [pygame.transform.scale(image, (C.SCREENWIDTH, C.SCREENHEIGHT)) for image in IC.menuBackground]
        self.index = 0
        self.maxIndex = len(self.cycle)
        self.animationCounter = 0
        self.menu_options = ["Continue", "New Game", "Load Game", "Settings", "Extras", "Quit"]
        self.font_size = 30
        self.font_color = (57, 255, 20)
        self.menu_x, self.menu_y = 450, 450
        self.menu_spacing = 40
        self.selected_option = 0
        self.animation_frame = 0
        self.frame_delay = 200
        self.clock = pygame.time.Clock()
        self.font_path = "assets/fonts/retro.ttf"
        self.font = pygame.font.Font(self.font_path, self.font_size)
        self.controlsCycle = IC.loadCycle("assets/animations/menu/controls")
        self.flashing_rect_color = self.font_color
        self.flashing_rect_size = (15, 25)
        self.flashing_rect_speed = 10
        self.flashing_rect_pos_y = self.menu_y  # Initial position Y
        self.flashing_rect_visible = True
        self.flashing_rect_timer = 0
        self.flashing_rect_delay = 300  # Milliseconds between each flash
        self.advance = False
        self.reverse = False
        pygame.mixer.music.load(soundManager.songNumber[2])#.wav or .ogg
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(1)
    
    def levelSkipCheck(self):
        if self.advance == True:
            C.LEVEL = Level1()
        elif self.reverse == True:
            self.reverse = False

    def draw(self):
        C.SCREEN.blit(self.cycle[self.animation_frame], (0, 0))
        for i, option in enumerate(self.menu_options):
            text_surface = self.font.render(option, True, self.font_color)
            text_rect = text_surface.get_rect(topleft=(self.menu_x, self.menu_y + i * self.menu_spacing))  # Left-aligned
            C.SCREEN.blit(text_surface, text_rect)
        if self.flashing_rect_visible:
            flashing_rect_pos_x = self.menu_x - self.flashing_rect_size[0] - 5  # Position to the left of the menu options
            flashing_rect_pos = (flashing_rect_pos_x, self.flashing_rect_pos_y)
            pygame.draw.rect(C.SCREEN, self.flashing_rect_color, (*flashing_rect_pos, *self.flashing_rect_size))

    def update(self):
        self.draw()
        self.flashing_rect_timer += C.DT
        if self.flashing_rect_timer >= self.flashing_rect_delay:
            self.flashing_rect_timer = 0
            self.flashing_rect_visible = not self.flashing_rect_visible

        self.animationCounter += C.DT  # Increment animation counter by delta time
        if self.animationCounter >= self.frame_delay:
            self.animation_frame = (self.animation_frame + 1) % len(self.cycle)  # Check if enough time has passed for next frame
            self.animationCounter = 0  # Reset animation counter

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    self.flashing_rect_pos_y = self.menu_y + self.selected_option * self.menu_spacing
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    self.flashing_rect_pos_y = self.menu_y + self.selected_option * self.menu_spacing
                elif event.key == pygame.K_RETURN:
                    selected_option_text = self.menu_options[self.selected_option]
                    if selected_option_text == "Continue":
                        # Continue selected, implement continuation logic
                        pass
                    elif selected_option_text == "New Game":
                    # New Game selected, start a new game by running main.py
                        C.LEVEL = Level1(self.player)
                    elif selected_option_text == "Load Game":
                    # Load Game selected, implement load game logic
                        pass
                    elif selected_option_text == "Settings":
                    # Settings selected, implement settings menu logic
                        self.menu_options = ["Graphics","Controls", "Audio", "Main Menu"]
                        self.selected_option = 0  # Reset selected option to the first one
                    # Handle other options...
                    elif selected_option_text == "Extras":
                    # Extras
                        self.menu_options = ["Mini Games", "Credits", "Main Menu", "Quit"]
                        self.selected_option = 0  # Reset selected option to the first one
                    # Handle other options...
                    elif selected_option_text == "Graphics":
                        self.menu_options = ["Resolution", "Fullscreen", "Main Menu", "Quit"]
                    elif selected_option_text == "Controls":
                        C.SCREEN.blit(self.controlsCycle[self.animation_frame], (500, 500))
                        self.animationCounter = 0  # Reset animation counter
                    elif selected_option_text == "Audio":
                        self.menu_options = ["Volume +", "Volume -","Mute", "Main Menu", "Quit"]
                    elif selected_option_text == "Main Menu":
                        self.menu_options = ["Continue", "New Game", "Load Game", "Settings", "Extras", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Mini Games":
                        self.menu_options = ["Dragon Poker", "Whack a Mole", "Brain Tetris", "Slide Puzzle", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Credits":
                        pass
                    elif selected_option_text == "Dragon Poker":
                        subprocess.run(["python", "pokey/eyepoker.py"])
                        sys.exit()
                    elif selected_option_text == "Whack a Mole":
                        pass
                    elif selected_option_text == "Brain Tetris":
                        subprocess.run(["python", "brainTetris.py"])
                        sys.exit()
                    elif selected_option_text == "Slide Puzzle":
                        subprocess.run(["python", "slidepuzzle.py"])
                        sys.exit()
                    elif selected_option_text == "Volume +":
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)  # Increase volume
                    elif selected_option_text == "Volume -":
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)  # Decrease volume
                    elif selected_option_text == "Mute":
                        pygame.mixer.music.set_volume(0)  # Mute volume
                    elif selected_option_text == "Resolution":
                        self.menu_options = ["1920x1080", "1600x900", "1280x720", "Full Screen" "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "1920x1080":
                        C.SCREEN = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                        self.menu_options = ["Resolution", "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "1600x900":
                        C.SCREEN = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
                        self.menu_options = ["Resolution", "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "1280x720":
                        C.SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                        self.menu_options = ["Resolution","Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Fullscreen":
                        C.SCREEN = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                        self.menu_options = ["Resolution", "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Quit":
                        pygame.quit()
                        sys.exit()


class Level1:
	def __init__(self, player):
		self.player = player

		self.player.cycle = IC.playerAnimation
		self.player.image = self.player.cycle[0]
		self.player.rect = self.player.image.get_rect()
		self.player.mask = pygame.mask.from_surface(self.player.image)

		self.player.rect.x = ((C.SCREENWIDTH * .5) - (self.player.rect.w * .5))
		self.player.rect.y = ((C.SCREENHEIGHT * .5) - (self.player.rect.h * .5))
		self.triggerTimer = 0
		self.triggerIndex = 0
		self.bgCounter = 0
		self.bgIndex = 0
		self.touchedDoor = False
		self.pressedUp = False
		self.openDoor = False

		self.lightCycle4Index = 0
		self.lCycle4 = IC.lightCycle4
		self.lightCycle4Counter = 0

		self.advance = False
		self.reverse = False

		pygame.mixer.music.load(soundManager.songNumber[0])#.wav or .ogg
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(.1)
		pygame.mixer.Channel(1).play(soundManager.level1)

	def levelSkipCheck(self):
		if self.advance == True:
			C.LEVEL = Level2(self.player)
		elif self.reverse == True:
			C.LEVEL = Level1(self.player)

	def drawBackground(self):
		C.SCREEN.blit(IC.level1Animation[self.bgIndex], (0,0))
		self.bgCounter += C.DT
		if self.bgCounter >= .3:
			if self.bgIndex == (len(IC.level1Animation)-1):
				self.bgIndex = 0
				self.bgCounter = 0
			else:
				self.bgIndex += 1
				self.bgCounter = 0

		C.SCREEN.blit(self.lCycle4[self.lightCycle4Index], (0,0))
		self.lightCycle4Counter += C.DT
		if self.lightCycle4Counter >= .4:
			if self.lightCycle4Index == (len(self.lCycle4)-1):
				self.lightCycle4Index = 0
				self.lightCycle4Counter = 0
			else:
				self.lightCycle4Index += 1
				self.lightCycle4Counter = 0

	def drawTrigger(self):
		if self.player.rect.right == C.SCREENWIDTH:	
			C.SCREEN.blit(IC.pressUpAnimation[self.triggerIndex], ((C.SCREENWIDTH - 350),(C.SCREENHEIGHT - 700)))
			self.triggerTimer += C.DT
			if self.triggerTimer >= .5:
				if self.triggerIndex == (len(IC.pressUpAnimation)-1):
					self.triggerIndex = 0
					self.triggerTimer = 0
				else:
					self.triggerIndex += 1
					self.triggerTimer = 0

	def handleTrigger(self):
		if self.player.rect.right == C.SCREENWIDTH:
			self.drawTrigger()

		if self.player.rect.right == C.SCREENWIDTH and self.player.pressedUp == True:
			pygame.mixer.Channel(1).pause()
			openTheDoor = door.OpenDoor()
			C.LEVEL = Level2(self.player)

	def update(self):
		self.levelSkipCheck()
		self.drawBackground()
		self.handleTrigger()

class Level2:
	def __init__(self, player):
		self.player = player

		self.player.cycle = IC.playerAnimation
		self.player.image = self.player.cycle[0]
		self.player.rect = self.player.image.get_rect()
		self.player.mask = pygame.mask.from_surface(self.player.image)

		self.player.rect.left = 0
		self.player.rect.bottom = C.SCREENHEIGHT
		self.triggerTimer = 0
		self.triggerIndex = 0
		self.bgCounter = 0
		self.bgIndex = 0
		self.playEgg = False
		self.easterEggCounter = 0
		self.touchedDoor = False
		self.pressedUp = False
		self.openDoor = False

		self.advance = False
		self.reverse = False

	def levelSkipCheck(self):
		if self.advance == True:
			pygame.mixer.Channel(1).pause()
			pygame.mixer.Channel(2).pause()
			pygame.mixer.music.stop()
			C.LEVEL = Level3(self.player)
		elif self.reverse == True:
			pygame.mixer.Channel(1).pause()
			pygame.mixer.Channel(2).pause()
			pygame.mixer.music.stop()
			C.LEVEL = Level1(self.player)

	def drawBackground(self):
		C.SCREEN.blit(IC.level2Animation[self.bgIndex], (0,0))
		self.bgCounter += C.DT
		if self.bgCounter >= .3:
			if self.bgIndex == (len(IC.level2Animation)-1):
				self.bgIndex = 0
				self.bgCounter = 0
			else:
				self.bgIndex += 1
				self.bgCounter = 0

	def drawTrigger(self):
			C.SCREEN.blit(IC.pressUpAnimation[self.triggerIndex], ((C.SCREENWIDTH - 350),(C.SCREENHEIGHT - 700)))
			self.triggerTimer += C.DT
			if self.triggerTimer >= .5:
				if self.triggerIndex == (len(IC.pressUpAnimation)-1):
					self.triggerIndex = 0
					self.triggerTimer = 0
				else:
					self.triggerIndex += 1
					self.triggerTimer = 0

	def handleTrigger(self):
		if self.player.rect.right == C.SCREENWIDTH:
			self.drawTrigger()

			if self.playEgg == False:
				self.easterEggCounter += C.DT			
			if self.easterEggCounter >= 10:
				pygame.mixer.Channel(2).play(soundManager.level2EasterEgg)	
				self.playEgg = True
				self.easterEggCounter = 0	

			if self.touchedDoor == False:
				pygame.mixer.music.stop()
				pygame.mixer.Channel(1).play(soundManager.level2)
				self.touchedDoor = True

		if self.player.rect.right == C.SCREENWIDTH and self.player.pressedUp == True and pygame.mixer.Channel(1).get_busy() == False:
			self.player.rect.left = 0
			pygame.mixer.Channel(2).pause()
			openTheDoor = door.OpenDoor()
			C.LEVEL = Level3(self.player)
		
	def update(self):
		self.levelSkipCheck()
		self.drawBackground()
		self.handleTrigger()

class Level3:
	def __init__(self, player):


		self.player = player
		self.player.inFlyingLevel = True

		self.player.cycle = IC.playerFlying
		self.player.image = self.player.cycle[0]
		self.player.rect = self.player.image.get_rect()
		self.player.mask = pygame.mask.from_surface(self.player.image)

		self.waveCounter = 0
		self.spawnEnemies = True
		self.parallaxCounter1 = 0
		self.parallaxCounter2 = 0
		self.parallaxCounter3 = 0
		self.parallaxCounter4 = 0
		self.parallaxCounter5 = 0
		self.advance = False
		self.reverse = False

		self.lightCycle1Index = 0
		self.lCycle1 = IC.lightCycle1
		self.lightCycle1Counter = 0

		self.lightCycle2Index = 0
		self.lCycle2 = IC.lightCycle2
		self.lightCycle2Counter = 0

		pygame.mixer.music.load(soundManager.songNumber[1])#.wav or .ogg
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(.1)



	def levelSkipCheck(self):
		if self.advance == True:
			pygame.mixer.Channel(1).pause()
			pygame.mixer.Channel(2).pause()
			pygame.mixer.music.stop()
			self.cleanUp()
			C.LEVEL = Level4(self.player)
		elif self.reverse == True:
			pygame.mixer.Channel(1).pause()
			pygame.mixer.Channel(2).pause()
			pygame.mixer.music.stop()
			self.cleanUp()
			C.LEVEL = Level2(self.player)

	def spawnEnemyWaves(self):
		if self.advance == False and self.reverse == False:
			if C.NUMBEROFENEMIES == 0:
				self.spawnEnemies = True

			if self.waveCounter == 0 and self.spawnEnemies == True:
				for x in range(5):
					neonlight = enemy.NeonLight()
					C.NUMBEROFENEMIES += 1
				self.spawnEnemies = False
				self.waveCounter += 1
			elif self.waveCounter == 1 and self.spawnEnemies == True:
				for x in range(5):
					trashCan = enemy.TrashCan()
					C.NUMBEROFENEMIES += 1
				self.spawnEnemies = False
				self.waveCounter += 1
			elif self.waveCounter == 2 and self.spawnEnemies == True:
				for x in range(5):
					boombox = enemy.BoomBox()
					C.NUMBEROFENEMIES += 1
				self.spawnEnemies = False
				self.waveCounter += 1
			elif self.waveCounter == 3 and self.spawnEnemies == True:
				for x in range(5):
					neonlight = enemy.NeonLight()
					trashCan = enemy.TrashCan()
					boombox = enemy.BoomBox()
					C.NUMBEROFENEMIES += 3
				self.spawnEnemies = False
				self.waveCounter = "done"

	def parallaxBackground(self):
		self.parallaxCounter1 -= 1
		self.parallaxCounter2 -= 3
		self.parallaxCounter3 -= 4
		self.parallaxCounter4 -= 8
		self.parallaxCounter5 -= 6

		C.SCREEN.blit(IC.clouds, (self.parallaxCounter1,0))
		C.SCREEN.blit(IC.clouds, ((self.parallaxCounter1+C.SCREENWIDTH),0))
		C.SCREEN.blit(IC.smog, (0,0))
		C.SCREEN.blit(IC.frontcity, (self.parallaxCounter2,0))
		C.SCREEN.blit(IC.frontcity, ((self.parallaxCounter2+C.SCREENWIDTH),0))
		C.SCREEN.blit(IC.smog, (0,0))

		C.SCREEN.blit(IC.city2, (self.parallaxCounter3,0))
		C.SCREEN.blit(IC.city2, ((self.parallaxCounter3+C.SCREENWIDTH),0))
		C.SCREEN.blit(self.lCycle2[self.lightCycle2Index], (self.parallaxCounter3,0))
		C.SCREEN.blit(self.lCycle2[self.lightCycle2Index], ((self.parallaxCounter3+C.SCREENWIDTH),0))
		self.lightCycle2Counter += C.DT
		if self.lightCycle2Counter >= .2:
			if self.lightCycle2Index == (len(self.lCycle2)-1):
				self.lightCycle2Index = 0
				self.lightCycle2Counter = 0
			else:
				self.lightCycle2Index += 1
				self.lightCycle2Counter = 0

		C.SCREEN.blit(IC.frontcity, (self.parallaxCounter5,0))
		C.SCREEN.blit(IC.frontcity, ((self.parallaxCounter5+C.SCREENWIDTH),0))
		C.SCREEN.blit(IC.smog, (0,0))

		C.SCREEN.blit(IC.city, (self.parallaxCounter4,0))
		C.SCREEN.blit(IC.city, ((self.parallaxCounter4+C.SCREENWIDTH),0))
		C.SCREEN.blit(self.lCycle1[self.lightCycle1Index], (self.parallaxCounter4,0))
		C.SCREEN.blit(self.lCycle1[self.lightCycle1Index], ((self.parallaxCounter4+C.SCREENWIDTH),0))
		self.lightCycle1Counter += C.DT
		if self.lightCycle1Counter >= .2:
			if self.lightCycle1Index == (len(self.lCycle1)-1):
				self.lightCycle1Index = 0
				self.lightCycle1Counter = 0
			else:
				self.lightCycle1Index += 1
				self.lightCycle1Counter = 0

		C.SCREEN.blit(IC.smog, (0,0))

		if self.parallaxCounter1 <= C.SCREENWIDTH * -1:
			self.parallaxCounter1 = 0
		elif self.parallaxCounter2 <= C.SCREENWIDTH * -1:
			self.parallaxCounter2 = 0
		elif self.parallaxCounter3 <= C.SCREENWIDTH * -1:
			self.parallaxCounter3 = 0
		elif self.parallaxCounter4 <= C.SCREENWIDTH * -1:
			self.parallaxCounter4 = 0
		elif self.parallaxCounter5 <= C.SCREENWIDTH * -1:
			self.parallaxCounter5 = 0

	def cleanUp(self):
		self.player.inFlyingLevel = False
		for x in C.enemy_sprite_list:
			x.destroy()
		for x in C.beam_list:
			x.destroy()
		for x in C.bullet_list:
			x.destroy()
		for x in C.particle_list:
			x.destroy()
		for x in C.explosion_list:
			x.destroy()
		for x in C.projectile_list:
			x.destroy()
        
	def update(self):
		self.levelSkipCheck()
		self.parallaxBackground()
		self.spawnEnemyWaves()
		if self.waveCounter == "done" and C.NUMBEROFENEMIES == 0:
			self.cleanUp()
			C.LEVEL = Level4(self.player)
			
		#scoreTimer += C.DT
		#if scoreTimer >= 1: #Every 1 second
		#	player.score += 100
		#	scoreTimer = 0

class Level4:
	def __init__(self, player):

#***************************************************************************************************************************************************#
#######################################Come back and figure out missing trees on upper layers########################################################
#***************************************************************************************************************************************************#
		self.player = player
		self.player.inOverheadLevel = True

		self.lightCycle3Index = 0
		self.lCycle3 = IC.lightCycle3
		self.lightCycle3Counter = 0		

		self.oldLady = NPC1.Npc1()
		self.emo = NPC2.Npc2()
		self.hippy = NPC3.Npc3()
		self.gymBro = NPC4.Npc4()
		self.pinkDress = NPC5.Npc5()

		IC.playerWalkRight = SVG.convert(target = self.player, cycleDirectory = IC.playerWalkRightDirectory, isMirrored = "no", scale = "overworld")
		IC.playerWalkLeft = SVG.convert(target = self.player,  cycleDirectory = IC.playerWalkLeftDirectory,  isMirrored = "no", scale = "overworld")
		IC.playerWalkDown = SVG.convert(target = self.player,  cycleDirectory = IC.playerWalkDownDirectory,  isMirrored = "no", scale = "overworld")
		IC.playerWalkUp = SVG.convert(target = self.player,  cycleDirectory = IC.playerWalkUpDirectory,  isMirrored = "no", scale = "overworld")
		IC.playerAnimation = SVG.convert(target = self.player,  cycleDirectory = IC.playerAnimationDirectory,  isMirrored = "no", scale = "overworld")

		self.player.rect.x = 81
		self.player.rect.y = 161
		self.gameMap = pytmx.load_pygame("assets/levels/level_4/socovillage.tmx")
		#for x in range(100):
		#	butterfly = bf.Butterfly()

		self.treeIndex = 0
		self.treeCounter = 0
		self.treeMax = 5

		self.waveIndex = 0
		self.waveCounter = 0
		self.waveMax = 8
		

		self.advance = False
		self.reverse = False

	def levelSkipCheck(self):
		if self.advance == True:
			self.player.inOverheadLevel = False
			self.cleanUp()
			C.LEVEL = Level5(self.player)
		elif self.reverse == True:
			self.cleanUp()
			C.LEVEL = Level3(self.player)

	def Render_Map(self, offset_x, offset_y, player):
		self.player = player

		for layer in self.gameMap.visible_layers:
			if isinstance(layer, pytmx.TiledTileLayer):
				if layer.name == "layer 0" or layer.name == "layer 1" or layer.name == "layer 2" or layer.name == "layer 3":

					for x, y, gid, in layer:

						MAP_X = x * self.gameMap.tilewidth  + offset_x
						MAP_Y = y * self.gameMap.tileheight + offset_y

						tile = self.gameMap.get_tile_image_by_gid(gid)
						if tile != None:
							C.SCREEN.blit(tile, (MAP_X, MAP_Y))

			if isinstance(layer, pytmx.TiledObjectGroup):
				if layer.name == "collision":
					for obj in layer:
						if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.player.rect) == True:
							if self.player.direction == "left":
								self.player.rect.left = obj.x + obj.width
							elif self.player.direction == "right":
								self.player.rect.right = obj.x
							elif self.player.direction == "up":
								self.player.rect.top = obj.y + obj.height
							elif self.player.direction == "down":
								self.player.rect.bottom = obj.y

	############################################################################################################################################
			if isinstance(layer, pytmx.TiledTileLayer):
				if layer.name == "trees 0" or layer.name == "trees 1" or layer.name == "trees 2" or layer.name == "waves":

					for x, y, image in layer.tiles():

						MAP_X = x * self.gameMap.tilewidth  + offset_x
						MAP_Y = y * self.gameMap.tileheight + offset_y

						if self.treeIndex > self.treeMax:
							self.treeIndex = 0

						if self.waveIndex > self.waveMax:
							self.waveIndex = 0

						for gid, props in self.gameMap.tile_properties.items():
							if image == self.gameMap.get_tile_image_by_gid(props['frames'][0].gid):
								#print (props)#Show all poperties
								#print (props['frames'][0].duration) #This is the animation duration
								#print (len(props['frames'])) #This is the number of animations
								image = self.gameMap.get_tile_image_by_gid(props['frames'][self.treeIndex].gid)
								C.SCREEN.blit(image, (MAP_X, MAP_Y))

		self.treeCounter += C.DT
		#print (C.TREECOUNTER)
		if self.treeCounter >= .5:
			self.treeIndex = self.treeIndex + 1 % len(props['frames'])
			self.treeCounter = 0

		if self.waveCounter >= .7:
			self.waveIndex = self.waveIndex + 1 % len(props['frames'])
			self.waveCounter = 0

	def drawLights(self, offset_x, offset_y):
		C.SCREEN.blit(self.lCycle3[self.lightCycle3Index], (offset_x,offset_y))
		self.lightCycle3Counter += C.DT
		if self.lightCycle3Counter >= .4:
			if self.lightCycle3Index == (len(self.lCycle3)-1):
				self.lightCycle3Index = 0
				self.lightCycle3Counter = 0
			else:
				self.lightCycle3Index += 1
				self.lightCycle3Counter = 0

	def cleanUp(self):
		self.player.inOverheadLevel = False
		self.player.speed = 400
		IC.playerWalkRight = SVG.convert(target = self.player, cycleDirectory = IC.playerWalkRightDirectory, isMirrored = "no", scale = "medium")
		IC.playerWalkLeft = SVG.convert(target = self.player, cycleDirectory = IC.playerWalkLeftDirectory,  isMirrored = "no", scale = "medium")
		#IC.playerWalkDown = SVG.convert(target = self.player,  cycleDirectory = IC.playerWalkDownDirectory,  isMirrored = "no", scale = "overworld")
		#IC.playerWalkUp = SVG.convert(target = self.player,  cycleDirectory = IC.playerWalkUpDirectory,  isMirrored = "no", scale = "overworld")
		IC.playerAnimation = SVG.convert(target = self.player, cycleDirectory = IC.playerAnimationDirectory,  isMirrored = "no", scale = "medium")
		for x in C.butterfly_list:
			x.destroy()
		for x in C.npc_list:
			x.destroy()

	def update(self):
		self.levelSkipCheck()
		#####################Possibly render map here instead of in main##############################
		#*****************************#self.Render_map()#********************************************#
		##############################################################################################

class Level5:
	def __init__(self, player):
		self.player = player
		self.player.inFlyingLevel = True

		self.player.cycle = IC.playerFlying
		self.player.image = self.player.cycle[0]
		self.player.rect = self.player.image.get_rect()
		self.player.mask = pygame.mask.from_surface(self.player.image)

		self.parallaxCounter1 = 0
		self.parallaxCounter2 = 0
		self.parallaxCounter3 = 0
		self.parallaxCounter4 = 0
		self.parallaxCounter5 = 0

		self.advance = False
		self.reverse = False

		pygame.mixer.music.load(soundManager.songNumber[1])#.wav or .ogg
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(.1)

	def parallaxBackground(self):
		self.parallaxCounter1 -= 1
		self.parallaxCounter2 -= 3
		self.parallaxCounter3 -= 4
		self.parallaxCounter4 -= 8
		self.parallaxCounter5 -= 6

		C.SCREEN.blit(IC.clouds, (self.parallaxCounter1,0))
		C.SCREEN.blit(IC.clouds, ((self.parallaxCounter1+C.SCREENWIDTH),0))
		C.SCREEN.blit(IC.smog, (0,0))
		C.SCREEN.blit(IC.mountains, (self.parallaxCounter2,0))
		C.SCREEN.blit(IC.mountains, ((self.parallaxCounter2+C.SCREENWIDTH),0))
		C.SCREEN.blit(IC.smog, (0,0))

		C.SCREEN.blit(IC.backForest, (self.parallaxCounter4,0))
		C.SCREEN.blit(IC.backForest, ((self.parallaxCounter4+C.SCREENWIDTH),0))
		C.SCREEN.blit(IC.middleForest, (self.parallaxCounter3,0))
		C.SCREEN.blit(IC.middleForest, ((self.parallaxCounter3+C.SCREENWIDTH),0))

		C.SCREEN.blit(IC.frontForest, (self.parallaxCounter5,0))
		C.SCREEN.blit(IC.frontForest, ((self.parallaxCounter5+C.SCREENWIDTH),0))



		if self.parallaxCounter1 <= C.SCREENWIDTH * -1:
			self.parallaxCounter1 = 0
		elif self.parallaxCounter2 <= C.SCREENWIDTH * -1:
			self.parallaxCounter2 = 0
		elif self.parallaxCounter3 <= C.SCREENWIDTH * -1:
			self.parallaxCounter3 = 0
		elif self.parallaxCounter4 <= C.SCREENWIDTH * -1:
			self.parallaxCounter4 = 0
		elif self.parallaxCounter5 <= C.SCREENWIDTH * -1:
			self.parallaxCounter5 = 0

	def update(self):
		self.parallaxBackground()
			
		#scoreTimer += C.DT
		#if scoreTimer >= 1: #Every 1 second
		#	player.score += 100
		#	scoreTimer = 0

