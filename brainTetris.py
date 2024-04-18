import pygame
import sys
import constants as C
import random
from SVGEditor import SVGImageLoader as SVG

class Tetris:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((C.SCREENWIDTH, C.SCREENHEIGHT))
        pygame.display.set_caption("Tetris")

        self.last_move_time = pygame.time.get_ticks()
        self.move_interval = 1000 

        self.clock = pygame.time.Clock()
        self.FPS = 30

        # Calculate the position to center the grid
        self.grid_size = 50
        self.grid_width = 10
        self.grid_height = 20
        self.grid_x = (C.SCREENWIDTH - 1270)
        self.grid_y = (C.SCREENHEIGHT - (self.grid_height * self.grid_size)) // 2

        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load("assets/sprites/BrainPieces/frame_00001.svg").convert_alpha()

        # Define brain piece sizes, offsets, and positions on the sprite sheet
        self.piece_info = {
            "_": {
                0: {"x": 0, "y": 0, "width": 200, "height": 50},
                90: {"x": 0, "y": 50, "width": 50, "height": 200},
                180: {"x": 0, "y": 0, "width": 200, "height": 50},
                270: {"x": 0, "y": 50, "width": 50, "height": 200},
            },
            "T": {
                0: {"x": 200, "y": 0, "width": 150, "height": 100},
                90: {"x": 250, "y": 100, "width": 100, "height": 150},
                180: {"x": 200, "y": 250, "width": 150, "height": 100},
                270: {"x": 200, "y": 350, "width": 100, "height": 150},
            },
            "L": {
                0: {"x": 350, "y": 0, "width": 100, "height": 150},
                90: {"x": 350, "y": 150, "width": 150, "height": 100},
                180: {"x": 350, "y": 250, "width": 100, "height": 150},
                270: {"x": 350, "y": 400, "width": 150, "height": 100},
            },
            "S": {
                0: {"x": 450, "y": 0, "width": 150, "height": 100},
                90: {"x": 500, "y": 100, "width": 100, "height": 150},
                180: {"x": 450, "y": 250, "width": 150, "height": 100},
                270: {"x": 500, "y": 350, "width": 100, "height": 150},
            },
            "Z": {
                0: {"x": 600, "y": 0, "width": 150, "height": 100},
                90: {"x": 650, "y": 100, "width": 100, "height": 150},
                180: {"x": 600, "y": 250, "width": 150, "height": 100},
                270: {"x": 600, "y": 350, "width": 100, "height": 150},
            },
            "O": {
                0: {"x": 800, "y": 0, "width": 100, "height": 100},
                90: {"x": 800, "y": 0, "width": 100, "height": 100},
                180: {"x": 800, "y": 0, "width": 100, "height": 100},
                270: {"x": 800, "y": 0, "width": 100, "height": 100},
            },
        }

        self.rotation_count = 0  # Track the number of times the piece has been rotated
        self.rotation_angle = 0  # Track the rotation angle
        self.current_brainPiece = random.choice(list(self.piece_info.keys()))
        self.piece_x = 0
        self.piece_y = 0
        self.key_pressed = False
        # Load rotated images from the sprite sheet only once during initialization
        self.rotated_images = self.load_rotated_images()

    def load_rotated_images(self):
        rotated_images = {}

        for piece_name, rotations in self.piece_info.items():
            rotated_images[piece_name] = {}
            for angle, info in rotations.items():
                rotated_piece = self.sprite_sheet.subsurface(
                    pygame.Rect(info["x"], info["y"], info["width"], info["height"])
                )
                rotated_images[piece_name][angle] = rotated_piece

        return rotated_images

    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0, 1))

        # Draw the grid
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                pygame.draw.rect(self.screen, (255, 255, 255), (self.grid_x + col * self.grid_size, self.grid_y + row * self.grid_size, self.grid_size, self.grid_size), 2)

        # Draw brain piece
        rotated_piece = self.rotated_images[self.current_brainPiece][self.rotation_angle]
        rotated_rect = rotated_piece.get_rect(center=(self.grid_x + self.piece_x + self.grid_size // 2, self.grid_y + self.piece_y + self.grid_size // 2))

        self.screen.blit(rotated_piece, rotated_rect.topleft)

    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_pressed = True
            elif event.type == pygame.KEYUP:
                self.key_pressed = False

    # Process the flag to perform actions
        if self.key_pressed:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.piece_x -= 50  # Move left by one column
            elif keys[pygame.K_RIGHT]:
                self.piece_x += 50  # Move right by one column
            elif keys[pygame.K_DOWN]:
                self.piece_y += 50  # Move down by one row
            elif keys[pygame.K_UP]:
            # Rotate the piece clockwise by 90 degrees
                self.rotation_angle = (self.rotation_angle + 90) % 360
                self.rotate_piece()

        self.check_collisions()

    def rotate_piece(self):
        # Count the number of times the up key has been pressed
        self.rotation_count = (self.rotation_count + 1) % 4
        # Set the rotation angle based on the count
        self.rotation_angle = self.rotation_count * 90

    def check_collisions(self):
        # Check if the piece is going out of the grid
        if self.piece_x < 0:
            self.piece_x = 0
        elif self.piece_x > (self.grid_width - 1) * self.grid_size:
            self.piece_x = (self.grid_width - 1) * self.grid_size

        if self.piece_y < 0:
            self.piece_y = 0
        elif self.piece_y > (self.grid_height - 1) * self.grid_size:
            self.piece_y = (self.grid_height - 1) * self.grid_size

    def conditions(self):
        # Implement game conditions (e.g., checking for lines) here
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            pygame.display.update()
            
            self.update()
            self.draw()

            self.clock.tick(self.FPS)

    def update(self):
        current_time = pygame.time.get_ticks()
        self.controls()
        # Check if it's time to move the piece down
        if current_time - self.last_move_time >= self.move_interval:
            self.piece_y += 50  # Move down by one row
            self.last_move_time = current_time

if __name__ == "__main__":
    tetris_game = Tetris()
    tetris_game.run()
