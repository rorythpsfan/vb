import pygame
import imageController as IC
import constants as C
class BaseNPC:
    def __init__(self):

        self.screen = C.SCREEN
        #self.BM = BM()
    def update(self, delta_time):
        self.elapsed_time += delta_time
        if self.elapsed_time >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.elapsed_time = 0
            self.position = [self.rect.x, self.rect.y]

    def draw(self):
        image = pygame.transform.flip(self.images[self.frame_index], self.isMirrored, False)
        self.screen.blit(image, self.position)

    def set_position(self, x, y):
        self.position = [x, y]

    def get_position(self):
        return tuple(self.position)


class grandmaNPC(BaseNPC):
    def __init__(self):
        
       self.image = IC.npc1Animation[0]
       self.cycle = IC.npc1Animation
       self.rect = self.image.get_rect()
       self.rect.x = ((C.SCREENWIDTH * .5) - (self.rect.w * .5))
       self.rect.y = ((C.SCREENHEIGHT * .5) - (self.rect.h * .5))
       self.lastX = self.rect.x
       self.lastY = self.rect.y
       super().__init__()


class EmoNPC(BaseNPC):
    def __init__(self, position=(0, 0)):
        svg_paths = [IC.npc20, IC.npc21]
        dialogue = "NPC says something else"
        super().__init__(self,position=position)


class gymBroNPC(BaseNPC):
    def __init__(self, position=(0, 0)):
        svg_paths = [IC.npc30, IC.npc31]
        dialogue = "Do you even lift bro? No? Thats cool, I'll do it for you."
        super().__init__(svg_paths, is_mirrored=False, position=position, dialogue=dialogue)


class hippyNPC(BaseNPC):
    def __init__(self, position=(0, 0)):
        svg_paths = [IC.npc40, IC.npc41]
        dialogue = "haha....totally rad to meet you brah"
        super().__init__(svg_paths, is_mirrored=True, position=position, dialogue=dialogue)


class picnicLadyNPC(BaseNPC):
    def __init__(self, position=(0, 0)):
        svg_paths = [IC.npc50, IC.npc51]
        dialogue = "The two most beautiful things in the world are Pink and Picnics with friends."
        super().__init__(svg_paths, is_mirrored=False, position=position, dialogue=dialogue)