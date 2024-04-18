import pygame
import sys
import os
import constants as C
import imageController as IC
import player as P
import time
class Items (pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        super().__init__()
        self.cycle = IC.sunglassesCycle
        self.image = self.cycle[self.index]
        self.rect = P.rect
        self.rect.x = P.rect.x
        self.rect.y = P.rect.y
        self.index = 0
        self.animationCounter = 0
        self.timer_start_time = 0
        self.effect_duration = 5 
    
    def draw(self):
        pos = (self.rect.x, self.rect.y)
        C.SCREEN.blit(self.image, pos)
    
        if P.overloaded == True:
            pass
        elif P.overloaded == False:
            self.animate()
        elif P.inFlyingLevel == True:
            pass
        elif P.inOverheadLevel == True:
            pass
    
    def animate(self):
        self.animationCounter += C.DT
        if self.animationCounter >= 0.1:
            if self.index == (len(self.cycle)-1):
                self.index = 0
                self.animationCounter = 0
            else:
                self.index += 1
                self.animationCounter = 0
    
    def effects(self):
        if self.image == IC.itemsCycle[0]:
            if not self.timer_started:
                self.timer_start_time = time.time()
                self.timer_started = True
            elapsed_time = time.time() - self.timer_start_time
            if elapsed_time >= self.effect_duration:
                P.health += 1
                self.timer_started = False
                self.timer_start_time = 0
            elif P.health >= 100:
                self.timer_start_time = 0
        
    
#
            
    def update(self):
        self.animate()
        self.draw()
        self.effects()
        
    
        
if __name__ == "__main__":
    items = Items(100, 100)