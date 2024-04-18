import pygame
import random
import imageController as IC
import constants as C

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, speedX, speedY, shadow_color):
        super().__init__()
        self.radius = random.randint(1, 2)
        self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.speedX = speedX
        self.speedY = speedY	
        self.color = (255,255,255)  # White color for particles

        self.changeDirectionCounter = random.uniform(0,1)
        self.stopCounter = 0
        self.stop = False
        self.killTimer = 0

        #C.all_sprites_list.add(self)		
        C.firefly_list.add(self)

        blueList = [
    (173, 216, 230),  # Light Baby Blue
    (191, 239, 255),  # Lighter Periwinkle
    (197, 233, 255),  # Light Carolina Blue
    (199, 230, 255),  # Light Sky Powder Blue
    (204, 232, 255),  # Light Powder Blue
    (197, 230, 255),  # Light Sky Blue
    (206, 236, 255),  # Light Pale Turquoise
]
        self.shadow_color = shadow_color
        if self.shadow_color == "multiblue":
            self.shadow_color = random.choice(blueList)
        elif self.shadow_color == "random":
            self.shadow_color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        elif self.shadow_color == "red":
            self.shadow_color = random.randint(0,255),0,0
        elif self.shadow_color == "green":
            self.shadow_color = 0,random.randint(0,255),0
        elif self.shadow_color == "blue":
            self.shadow_color = 0,0,random.randint(0,255)
        elif self.shadow_color == "white":
            self.shadow_color = 0,0,0

        self.alpha = random.randint(150, 200)  # Random alpha value between 200 and 255 for particles

        self.frame_counter = 0
        self.frames_to_change_alpha = 10

    def draw(self, SCREEN, camera):

        self.rect.x += self.speedX * C.DT
        self.rect.y += self.speedY * C.DT

        self.pos = ((self.rect.x) - camera.position.x,(self.rect.y) - camera.position.y)

        self.changeDirectionCounter += C.DT

        if self.changeDirectionCounter >= 2:
            self.stop = True
            self.speedX = 0
            self.speedY = 0
        if self.stop == True:
            self.stopCounter += C.DT
            if self.stopCounter >= 1:			
                self.speedX = random.randint(-50,50)
                self.speedY = random.randint(-50,50)
                self.stop = False
                self.stopCounter = 0
                self.changeDirectionCounter = 0

        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (self.color[0],self.color[1],self.color[2], self.alpha), (self.radius, self.radius), self.radius)
        C.SCREEN.blit(surface, (self.pos[0] - self.radius, self.pos[1] - self.radius))

        if self.frame_counter % self.frames_to_change_alpha == 0:
            # Change alpha to a random value between 50 and 200
            self.alpha2 = random.randint(50, 150)

        shadow_color = (self.shadow_color[0],self.shadow_color[1],self.shadow_color[2], self.alpha2)
        shadow_radius = random.randint(2,5) 
        shadow_surface = pygame.Surface((shadow_radius * 2, shadow_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(shadow_surface, shadow_color, (shadow_radius, shadow_radius), shadow_radius)
        C.SCREEN.blit(shadow_surface, (int(self.pos[0]) - shadow_radius, int(self.pos[1]) - shadow_radius))

        # Increment the frame counter
        self.frame_counter += 1

		#C.SCREEN.blit(self.image, pos)

    def recursiveWalls(self):
        if self.rect.x > 2390:
            self.rect.x = 10
        elif self.rect.y > 1590:
            self.rect.y = 10
        elif self.rect.x < 10:
            self.rect.x = 2390
        elif self.rect.y < 10:
            self.rect.y = 1590

    def destroy(self):
        C.all_sprites_list.remove(self)
        C.firefly_list.remove(self)
        self.kill()

    def update(self):
        self.recursiveWalls()
        self.killTimer += C.DT
        if self.killTimer >= 360:
            self.destroy()

