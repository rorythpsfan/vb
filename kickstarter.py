import pygame
import sys
import constants as C
import imageController as IC

class KickstarterLink:
    def __init__(self):
        pygame.init()

        self.cycle = IC.kickstarterCycle
        self.index = 0
        self.counter = 0
        self.button_color = (255, 0, 0, 0)  # Setting alpha to 0 for full transparency
        self.button_width, self.button_height = 300, 200
        self.button_rect = pygame.Rect(C.SCREENWIDTH - self.button_width - 20, C.SCREENHEIGHT - self.button_height - 20, self.button_width, self.button_height)
        self.link = "https://www.kickstarter.com/projects/rorythpsfan/1710054623?ref=96f2tm&token=f6ce10f4"
        self.isVisible = False

    def animate(self):

        self.counter += C.DT
        if self.counter >= .3:
            if self.index == (len(self.cycle) - 1):
                self.index = 0
                self.counter = 0
            else:
                self.index += 1
                self.counter = 0

        C.SCREEN.blit(self.cycle[self.index], (0, 0))
        button_surface = pygame.Surface((self.button_width, self.button_height), pygame.SRCALPHA)
        button_surface.fill(self.button_color)
        C.SCREEN.blit(button_surface, (C.SCREENWIDTH - self.button_width - 20, C.SCREENHEIGHT - self.button_height - 20))

    def update(self):


        self.animate()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.isVisible = False






