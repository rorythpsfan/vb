import pygame
import time

pygame.display.set_caption('sAd')

SCREENWIDTH = 1920
SCREENHEIGHT = 1080
SCREEN = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT],32, vsync=1)
CLOCK = pygame.time.Clock()

pygame.font.init()
BATTLEFONT = pygame.font.SysFont("assets/fonts/retro.ttf", 32, bold = True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHTPINK = (255, 105, 180)
RED = (255,0,0)
SWEETBLUE = (0,102,204)

QUIT = False
FPS = 60
DT = 0
PAUSED = False
LEVEL = 0

GAMEOVER = False
gameoverCounter = 0
gameoverIndex = 0

all_sprites_list = pygame.sprite.Group()
enemy_sprite_list = pygame.sprite.Group()
player_sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
beam_list = pygame.sprite.Group()
particle_list = pygame.sprite.Group()
butterfly_list = pygame.sprite.Group()
firefly_list = pygame.sprite.Group()
npc_list = pygame.sprite.Group()
fade_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
projectile_list = pygame.sprite.Group()
NUMBEROFENEMIES = 0
