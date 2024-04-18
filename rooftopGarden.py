import pygame
from lol import Water

class RooftopGarden:
    def __init__(self):
        # Define screen size
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.SRCALPHA)
        
        # Define square size
        self.SQUARE_SIZE = 80
        self.image = pygame.image.load("map idea.png").convert_alpha()
        
        # Define grid size
        self.GRID_SIZE = 25
        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0, 0)
        
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Rooftop Garden")
        pygame.font.Font("VBfont1.ttf", 36)
        
        # Initialize grid colors
        self.grid_colors = [[self.WHITE] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        
        # Initialize inventory colors
        self.inventory_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
                                 (255, 0, 255), (0, 255, 255), (128, 0, 128), (128, 128, 0), 
                                 (0, 128, 128), (128, 128, 128)]
        self.selected_color = self.inventory_colors[0]
        
        # Camera variables
        self.camera_x = 0
        self.camera_y = 0
        self.dragging = False
        self.last_mouse_pos = (0, 0)
        
        self.left_click = False
        self.right_click = False

    def draw(self):
        for y in range(self.GRID_SIZE):
            for x in range(self.GRID_SIZE):
                pygame.draw.rect(self.SCREEN, self.grid_colors[y][x],
                                 (x * self.SQUARE_SIZE + self.camera_x, y * self.SQUARE_SIZE + self.camera_y,
                                  self.SQUARE_SIZE, self.SQUARE_SIZE), 1)
        for i, color in enumerate(self.inventory_colors):
            pygame.draw.rect(self.SCREEN, color,
                             (self.SCREEN_WIDTH - 80, i * 80, 80, 80))
            if color == self.selected_color:
                pygame.draw.rect(self.SCREEN, (255, 255, 255),
                                 (self.SCREEN_WIDTH - 80, i * 80, 80, 80), 3)

    def controls(self):
        if self.left_click == True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = (mouse_x - self.camera_x) // self.SQUARE_SIZE
            grid_y = (mouse_y - self.camera_y) // self.SQUARE_SIZE
            if 0 <= grid_x < self.GRID_SIZE and 0 <= grid_y < self.GRID_SIZE:
                self.grid_colors[grid_y][grid_x] = self.selected_color
            self.left_click = False

        if self.right_click == True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            inventory_index = mouse_y // self.SQUARE_SIZE
            if 0 <= inventory_index < len(self.inventory_colors):
                self.selected_color = self.inventory_colors[inventory_index]
            self.right_click = False
    
    def pause (self):
        pygame.time.wait()
            
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.left_click = True
                        self.controls()
                    elif event.button == 3:
                        self.right_click = True # Right click
                        self.controls()
                    elif event.button == 2:  # Middle click
                        self.dragging = True
                        self.last_mouse_pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 2:
                        self.dragging = False
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        dx, dy = pygame.mouse.get_pos()[0] - self.last_mouse_pos[0], pygame.mouse.get_pos()[1] - self.last_mouse_pos[1]
                        self.camera_x += dx
                        self.camera_y += dy
                        self.last_mouse_pos = pygame.mouse.get_pos()
                elif event.type == pygame.K_ESCAPE:
                    self.pause()
            self.SCREEN.fill(self.WHITE)
            self.SCREEN.blit(self.image, (self.camera_x, self.camera_y))
            self.draw()
            water = Water(screen_width=800, screen_height=600)  # Set the desired size
            water.run()
            
            pygame.display.flip()
            
        pygame.quit()


if __name__ == "__main__":
    game = RooftopGarden()
    game.run()