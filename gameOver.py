import pygame
import constants as C
import imageController as IC

C.GAMEOVER = False
C.gameoverCounter = 0
C.gameoverIndex = 0

def show_game_over_screen():

	C.SCREEN.blit(IC.game_over[C.gameoverIndex], (0, 0))
	C.gameoverCounter += C.DT
	if C.gameoverCounter >= 0.2:
		if C.gameoverIndex == (len(IC.game_over) - 1):
			C.gameoverIndex = 0
			C.gameoverCounter = 0
		else:
			C.gameoverIndex += 1
			C.gameoverCounter = 0



