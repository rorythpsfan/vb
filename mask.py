import pygame
import imageController as IC
import constants as C

class Mask(pygame.sprite.Sprite):
    """Player Class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = IC.socovillageMask
        self.trueImage = IC.socovillageMap
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # Mask for pixel-perfect collisions
        self.mask = pygame.mask.from_surface(self.image)



        #C.all_sprites_list.add(self)
        C.mask_list.add(self)

    def draw(self, SCREEN, camera):
        pos = (self.rect.x - camera.position.x,
            self.rect.y - camera.position.y)

        C.SCREEN.blit(self.image, pos)
        C.SCREEN.blit(self.trueImage, pos)		


    def update(self):
        pass
