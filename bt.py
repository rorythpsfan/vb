import pygame
import sys
import random

class Tetris:
    def __init__(self):
        pygame.init()

        self.screen_width = 400
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()
        self.fps = 30

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

        self.grid_size = 25
        self.grid_width = self.screen_width // self.grid_size
        self.grid_height = self.screen_height // self.grid_size

        # Initialize the grid with zeros
        self.grid = [[0] * self.grid_width for _ in range(self.grid_height)]

        self.current_brain_piece = None
        self.rotation_angle = 0
        self.piece_x = self.grid_width // 2
        self.piece_y = 0

        self.spawn_piece()

    def spawn_piece(self):
        self.current_brain_piece = random.choice(list(self.piece_info.keys()))
        self.rotation_angle = 0
        self.piece_x = self.grid_width // 2
        self.piece_y = 0

    def rotate_piece(self):
        self.rotation_angle = (self.rotation_angle + 90) % 360

    def draw_grid(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] != 0:
                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 255),
                        (col * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size),
                    )

    def draw_current_piece(self):
        piece_rotations = self.piece_info[self.current_brain_piece]
        rotated_piece = self.get_rotated_piece()
        for row in range(rotated_piece.get_height()):
            for col in range(rotated_piece.get_width()):
                if rotated_piece.get_at((col, row)) != (0, 0, 0, 0):
                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 255),
                        (
                            (self.piece_x + col) * self.grid_size,
                            (self.piece_y + row) * self.grid_size,
                            self.grid_size,
                            self.grid_size,
                        ),
                    )

    def get_rotated_piece(self):
        piece_rotations = self.piece_info[self.current_brain_piece]
        return pygame.transform.rotate(self.sprite_sheet, self.rotation_angle)

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.draw_grid()
        self.draw_current_piece()

        pygame.display.flip()

    def update(self):
        self.check_collisions()
        self.move_down()

    def check_collisions(self):
        rotated_piece = self.get_rotated_piece()
        for row in range(rotated_piece.get_height()):
            for col in range(rotated_piece.get_width()):
                if (
                    self.piece_y + row >= self.grid_height
                    or self.piece_x + col < 0
                    or self.piece_x + col >= self.grid_width
                    or (self.piece_y + row < self.grid_height and self.piece_x + col < self.grid_width
                        and self.grid[self.piece_y + row][self.piece_x + col] != 0 and rotated_piece.get_at((col, row)) != (0, 0, 0, 0))
                ):
                    self.merge_piece()
                    self.spawn_piece()

    def move_down(self):
        self.piece_y += 1

    def merge_piece(self):
        rotated_piece = self.get_rotated_piece()
        for row in range(rotated_piece.get_height()):
            for col in range(rotated_piece.get_width()):
                if rotated_piece.get_at((col, row)) != (0, 0, 0, 0):
                    grid_row = self.piece_y + row
                    grid_col = self.piece_x + col

                    # Check if the piece is within the grid bounds
                    if 0 <= grid_row < self.grid_height and 0 <= grid_col < self.grid_width:
                        self.grid[grid_row][grid_col] = 1
                    else:
                        # Handle the case where the piece is out of bounds
                        print("Game Over: Piece out of bounds")
                        pygame.quit()
                        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_sideways(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.move_sideways(1)
                    elif event.key == pygame.K_DOWN:
                        self.move_down()
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()

            self.update()
            self.draw()

            self.clock.tick(self.fps)

    def move_sideways(self, direction):
        self.piece_x += direction
        if self.check_collision():
            self.piece_x -= direction

    def check_collision(self):
        rotated_piece = self.get_rotated_piece()
        for row in range(rotated_piece.get_height()):
            for col in range(rotated_piece.get_width()):
                if (
                    self.piece_y + row >= self.grid_height
                    or self.piece_x + col < 0
                    or self.piece_x + col >= self.grid_width
                    or (self.piece_y + row < self.grid_height and self.piece_x + col < self.grid_width
                        and self.grid[self.piece_y + row][self.piece_x + col] != 0 and rotated_piece.get_at((col, row)) != (0, 0, 0, 0))
                ):
                    return True
        return False

if __name__ == "__main__":
    tetris_game = Tetris()
    tetris_game.run()
