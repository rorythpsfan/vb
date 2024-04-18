import pygame
import constants as C
from pathlib import Path
import os

def loadCycle(cycleDirectory):
	modifiedAnimationCycle = []
	folder_dir = cycleDirectory
	isSVG = False

	for fname in os.listdir(folder_dir):
		if fname.endswith('.svg'):
			isSVG = True

	if isSVG == True:
		images = Path(folder_dir).glob('*.svg')
	else:
		images = Path(folder_dir).glob('*.png')

	for image in images:
		nextImage = pygame.image.load(image).convert_alpha()
		modifiedAnimationCycle.append(nextImage)

	message = ("Loaded cycle from folder " + str(cycleDirectory) + ("   :)"))
	print (message)
	return modifiedAnimationCycle

##### MENU ANIMATIONS ####
menuBackground = loadCycle("assets/animations/menu/menuCycle/")
mainMenuAnimation = loadCycle("assets/animations/menu/mainMenu/")
game_over = loadCycle("assets/animations/menu/gameOver/")
controlsMenu = loadCycle("assets/animations/menu/controls/")
##### HUD ANIMATIONS#####

hudAnimation = loadCycle("assets/animations/hud/")

##### PLAYER ANIMATIONS ####

playerAnimation = loadCycle("assets/animations/player/playerStand/")
playerAnimationDirectory = "assets/animations/player/playerStand/"

playerFlying = loadCycle("assets/animations/player/playerFlying/")
playerFlyingDirectory = "assets/animations/player/playerFlying/"

playerWalkRight = loadCycle("assets/animations/player/playerWalkRight/")
playerWalkRightDirectory = "assets/animations/player/playerWalkRight/"

playerWalkLeft = loadCycle("assets/animations/player/playerWalkLeft/")
playerWalkLeftDirectory = "assets/animations/player/playerWalkLeft/"

playerWalkDown = loadCycle("assets/animations/player/playerWalkDown/")
playerWalkDownDirectory = "assets/animations/player/playerWalkDown/"

playerWalkUp = loadCycle("assets/animations/player/playerWalkUp/")
playerWalkUpDirectory = "assets/animations/player/playerWalkUp/"

playerOverloaded = loadCycle("assets/animations/player/playerOverloaded/")

##### LEVEL ANIMATIONS ####

level1Animation = loadCycle("assets/levels/level_1/")

level2Animation = loadCycle("assets/levels/level_2/")

city = pygame.image.load("assets/levels/Level_3/frame_00004.svg").convert_alpha()
city2 = pygame.image.load("assets/levels/Level_3/frame_00005.svg").convert_alpha()
clouds = pygame.image.load("assets/levels/Level_3/frame_00001.svg").convert_alpha()
frontcity = pygame.image.load("assets/levels/Level_3/frame_00003.svg").convert_alpha()
smog = pygame.image.load("assets/levels/Level_3/frame_00009.svg").convert_alpha()

frontForest = pygame.image.load("assets/levels/Level_5/forest/frame_00001.png").convert_alpha()
middleForest = pygame.image.load("assets/levels/Level_5/forest/frame_00002.png").convert_alpha()
backForest = pygame.image.load("assets/levels/Level_5/forest/frame_00003.png").convert_alpha()
mountains = pygame.image.load("assets/levels/Level_5/forest/frame_00004.png").convert_alpha()



doorAnimation = loadCycle("assets/animations/doorOpen/")

battleAnimation = loadCycle("assets/animations/battleAnimations/")
waterAnimation = loadCycle("assets/animations/water/")
##### PROMPT ANIMATIONS#####

pressUpAnimation = loadCycle("assets/animations/trigger/pressUp/")

##### ENEMY ANIMATIONS ####

neonLight = loadCycle("assets/sprites/neonlight/")
neonLightDirectory = "assets/sprites/neonlight/"

boomBox = loadCycle("assets/sprites/boomboxframes/")
boomBoxDirectory = "assets/sprites/boomboxframes/"

trashCan = loadCycle("assets/sprites/trashcanframes")
trashCanDirectory = "assets/sprites/trashcanframes"

##### NPC ANIMATIONS #####

npc1Animation = loadCycle("assets/animations/NPCs/NPC1/")
npc1AnimationDirectory = "assets/animations/NPCs/NPC1/"

npc2Animation = loadCycle("assets/animations/NPCs/NPC2/")
npc2AnimationDirectory = "assets/animations/NPCs/NPC2/"

npc3Animation = loadCycle("assets/animations/NPCs/NPC3/")
npc3AnimationDirectory = "assets/animations/NPCs/NPC3/"

npc4Animation = loadCycle("assets/animations/NPCs/NPC4/")
npc4AnimationDirectory = "assets/animations/NPCs/NPC4/"

npc5Animation = loadCycle("assets/animations/NPCs/NPC5/")
npc5AnimationDirectory = "assets/animations/NPCs/NPC5/"

butterflyAnimation = loadCycle("assets/sprites/butterfly/")
butterflyAnimationDirectory = "assets/sprites/butterfly/"

##### PROJECTILE ANIMATIONS #####

beamCycle = loadCycle("assets/projectiles/beam/")
beamCycleDirectory = "assets/projectiles/beam/"

projectileOneCycle = loadCycle("assets/projectiles/projectile1/")

spitballCycle = loadCycle("assets/projectiles/spitball/")

soundWaveCycle = loadCycle("assets/projectiles/soundWave/")
soundWaveCycleDirectory = "assets/projectiles/soundWave/"

toxicGasCycle = loadCycle("assets/projectiles/toxicGas/")
toxicGasCycleDirectory = "assets/projectiles/toxicGas/"
##### EXPLOSION ANIMATIONS #####

explosionOneCycle = loadCycle("assets/explosions/explosion1/")

powAnimationCycle = loadCycle("assets/explosions/pow/")
powAnimationCycleDirectory = "assets/explosions/pow/"

boomAnimationCycle = loadCycle("assets/explosions/boom/")
boomAnimationCycleDirectory = "assets/explosions/boom/"

spitsplosionCycle = loadCycle("assets/explosions/spitsplosion/")

##### ANIMATED SEQUENCES #####
titleScreenAnimation = loadCycle("assets/animations/titleScreen/")
lake = pygame.image.load("assets/animations/lakeAnim/frame_00001.png").convert_alpha()
static = loadCycle("assets/animations/static")
##### LIGHTING #####
lightCycle1 = loadCycle("assets/levels/level_3/lightCycle1")
lightCycle2 = loadCycle("assets/levels/level_3/lightCycle2")
lightCycle3 = loadCycle("assets/levels/level_4/lightCycle3")
lightCycle4 = loadCycle("assets/levels/level_1/lightCycle4")

##### KICKSTARTER ANIMATION #####
kickstarterCycle = loadCycle("assets/animations/demo/")


##### ITEMS ANIMATION ##### 
sunglassesCycle = loadCycle("assets/animations/items/sunglasses/")



