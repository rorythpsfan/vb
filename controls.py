import pygame
import sys
import subprocess
import constants as C
# Initialize Pygame
pygame.init()

# Define screen dimensions
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Define constants
BG_COLOR = (255, 255, 255)
FONT_SIZE = 72  # Adjust font size for larger screen
MENU_X, MENU_Y = WIDTH // 2, HEIGHT // 2 - 100  # Centered positioning
MENU_SPACING = 80  # Increased spacing for larger screen

# Create the screen
screen = C.SCREEN
pygame.display.set_caption("Controls Page")

# Animation frame delay (in milliseconds)
frame_delay = 600  # Adjust this value to control the animation speed

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Controls page loop
animation_frame = 0  # Initialize animation frame

# Frame menu images
frames = [
    pygame.image.load("/assets/animations/controls/frame_00001.png"),
    pygame.image.load("/assets/animations/controls/frame_00002.png"),
    pygame.image.load("/assets/animations/controls/frame_00003.png")
]

running = True
last_frame_time = pygame.time.get_ticks()  # Get the current time in milliseconds
while running:
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    if current_time - last_frame_time >= frame_delay:
         last_frame_time += frame_delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Return to menu.py when ESC key is pressed
                subprocess.run(["python", "menu.py"])
                sys.exit()

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw animation frames onto the screen
    screen.blit(frames[animation_frame], (0, 0))

    # Update animation frame
    animation_frame = (animation_frame + 1) % len(frames)
    
    clock.tick(5)

    pygame.display.flip()

# Quit Pygame and exit the script
pygame.quit()
sys.exit()
