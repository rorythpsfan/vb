import pygame
import numpy as np
import random
import os
class Water:
    def __init__(self):
        # Define your SCREEN_SIZE constant
        self.SCREEN_SIZE = 2400, 1600
        # Initialize Pygame
        pygame.init()
        # Set up the display
        self.SCREEN = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("Water?")
        # Generate list of shifts
        self.shifts = list(range(1, 20, 1))
        # Initialize frame index and frame delay
        self.frame_index = 2
        self.frame_delay = 80  # Adjust this value to control the frame rate
        # Set running flag
        self.running = True
        self.lake = pygame.image.load("assets/animations/lakeAnim/frame_00001.png").convert_alpha()

        # Pre-calculate shades of blue
        self.blues = [
            (0, 160, 255),
            (0, 170, 255),
            (0, 180, 255),
            (0, 190, 255),
            (0, 200, 255),
            (0, 220, 255),
            (0, 230, 255),
            (255, 255, 255)
        ]

    def generate_pattern(self, width, height, shift):
        x = np.arange(width).reshape(1, width)
        y = np.arange(height).reshape(height, 1)

        layer1 = np.sin(x / 16.0 + shift) * 0.02
        layer2 = np.sin(y / 8.0 + shift) * 0.02
        layer3 = np.sin((x + y) / 16.0 + shift) * 0.02
        layer4 = np.sin(np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2) / 8.0 + shift) * 0.02
        layer5 = np.sin(x / 16.0 + shift) * 0.02
        layer6 = np.sin(y / 8.0 + shift) * 0.02
        layer7 = np.sin((x + y) / 16.0 + shift) * 0.02
        layer8 = np.sin(np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2) / 8.0 + shift) * 0.02

        # Combine layers and normalize
        arr = layer1 + layer2 + layer3 + layer4 + layer5 + layer6 + layer7 + layer8
        arr = np.sin(arr * np.pi)

        # Normalize to 0-255 and return as an integer array
        arr = (arr + 1) * 128
        return np.array(arr, dtype=np.uint8)

    def convert_scale(self, pattern_arr):
        # Normalize pattern_arr to range [0, 1]
        normalized_arr = pattern_arr / 255.0

        # Map each value in normalized_arr to a shade of blue based on its darkness
        shade_indices = (normalized_arr * (len(self.blues) - 1)).astype(int)
        colored_arr = np.array([self.blues[idx] for idx in shade_indices.flatten()], dtype=np.uint8)
        colored_arr = colored_arr.reshape(pattern_arr.shape[0], pattern_arr.shape[1], 3)

        return colored_arr

    def seafoam(self, surface):
        # Create a new surface with per-pixel alpha
        foam_surface = pygame.Surface(self.SCREEN_SIZE, pygame.SRCALPHA)
        # Add seafoam to the surface
        num_seafoam = random.randint(150, 250)
        for _ in range(num_seafoam):
            radius = random.randint(1, 4)
            x_pos = random.randint(radius, self.SCREEN_SIZE[0] - radius)
            y_pos = random.randint(radius, self.SCREEN_SIZE[1] - radius)
            # Generate a random alpha value within the desired range
            random_alpha = random.randint(30, 100)
            pygame.draw.circle(foam_surface, (255, 255, 255, random_alpha), (x_pos, y_pos), radius)
    # Blit the seafoam surface onto the original surface
        surface.blit(foam_surface, (0, 0))

    def save_frames_as_png(self, num_frames=20):
        # Create a directory to save the frames if it doesn't exist
        if not os.path.exists("frames"):
            os.makedirs("frames")

        # Capture and save the first 'num_frames' frames as PNG files
        for frame_index in range(num_frames):
            current_shift = self.shifts[frame_index % len(self.shifts)]
            pattern_arr = self.generate_pattern(self.SCREEN_SIZE[0], self.SCREEN_SIZE[1], current_shift)
            pattern_arr = self.convert_scale(pattern_arr)

            surface = pygame.surfarray.make_surface(pattern_arr)
            surface = pygame.transform.smoothscale(surface, self.SCREEN_SIZE)

            filename = os.path.join("frames", f"frame_{frame_index:05}.png")
            pygame.image.save(surface, filename)
    

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Get the current shift value based on the frame index
            current_shift = self.shifts[self.frame_index % len(self.shifts)]

            # Generate pattern for the current frame
            pattern_arr = self.generate_pattern(self.SCREEN_SIZE[0], self.SCREEN_SIZE[1], current_shift)

            # Convert to bluescale
            pattern_arr = self.convert_scale(pattern_arr)

            # Map the array values to a Pygame surface
            surface = pygame.surfarray.make_surface(pattern_arr)
            surface = pygame.transform.smoothscale(surface, self.SCREEN_SIZE)
            #surface = pygame.transform.gaussian_blur(surface, 1)
            # Add seafoam
            #self.seafoam(surface)

            # Blit the surface onto the screen
            self.SCREEN.blit(surface, (0, 0))
            #self.SCREEN.blit(self.lake, (0, 0))
            # Update the display
            pygame.display.flip()

            # Increment frame index
            self.frame_index += 1

            # Control the frame rate
            pygame.time.delay(self.frame_delay)

        # Quit Pygame
        pygame.quit()

# Create an instance of the PatternAnimation class and run the animation
if __name__ == "__main__":
    water = Water()
    water.save_frames_as_png()
    water.run()