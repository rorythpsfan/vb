import pygame
import random  # Import the random module
import constants as C

class LightningEffect:
    def __init__(self, screen):
        self.screen = screen
        self.lightning_surface = pygame.Surface((C.SCREENWIDTH, C.SCREENHEIGHT))  # Create a surface the size of the screen
        self.lightning_surface.set_alpha(0)  # Set initial alpha to 0 (fully transparent)
        self.lightning_surface.fill((255, 255, 255))  # Fill the surface with white color
        self.counter = 0  # Counter to keep track of frames
        self.max_alpha_reached = False  # Flag to track if maximum alpha has been reached
        self.random_delay = random.randint(50, 150)  # Random delay between 50 and 150 frames

    
    def update(self):
        self.counter += 1
        if not self.max_alpha_reached:  # Check if maximum alpha has not been reached
            current_alpha = self.lightning_surface.get_alpha()
            if current_alpha < 255:  # Increase alpha up to 255 (fully opaque)
                new_alpha = min(current_alpha +1, 255)  # Increase alpha by 40 (adjust the increment as needed for faster change)
                self.lightning_surface.set_alpha(new_alpha)
            else:  # Set flag when maximum alpha is reached
                self.max_alpha_reached = True
                self.lightning_surface.set_alpha(0)  # Reset alpha to 0
                self.random_delay = random.randint(10, 150)  # Generate a new random delay
        else:  # If maximum alpha has been reached
            if self.counter >= self.random_delay:  # Check if random delay has passed
                self.max_alpha_reached = False  # Reset the flag
                self.counter = 0  # Reset the counter

    def draw_lightning_bolt(self):
        bolt_color = (255, 255, 255)  # Base color for the lightning bolt
        max_depth = 8  # Maximum depth for branching
        branch_chance = 5  # Percentage chance of branching
        fork_chance = 10  # Percentage chance of forking

        start_x = random.randint(0, C.SCREENWIDTH)  # Random start x-coordinate
        start_y = 0  # Start y-coordinate at the top of the screen
        end_x = random.randint(0, C.SCREENWIDTH)  # Random end x-coordinate
        end_y = C.SCREENHEIGHT  # End y-coordinate at the bottom of the screen

        self.draw_branching_lightning(start_x, start_y, end_x, end_y, bolt_color, max_depth, branch_chance, fork_chance)

    def draw_branching_lightning(self, start_x, start_y, end_x, end_y, color, depth, branch_chance, fork_chance):
        if depth <= 0:
            pygame.draw.line(self.lightning_surface, color, (start_x, start_y), (end_x, end_y), 2)  # Draw the main bolt
            return

        mid_x = (start_x + end_x) // 2  # Calculate the midpoint x-coordinate
        mid_y = (start_y + end_y) // 2  # Calculate the midpoint y-coordinate

        if start_x < end_x:
            mid_x += random.randint(-20, 20)  # Introduce randomness to the x-coordinate
        if start_y < end_y:
            mid_y += random.randint(-20, 20)  # Introduce randomness to the y-coordinate

        self.draw_branching_lightning(start_x, start_y, mid_x, mid_y, color, depth - 1, branch_chance, fork_chance)  # Draw left branch
        self.draw_branching_lightning(mid_x, mid_y, end_x, end_y, color, depth - 1, branch_chance, fork_chance)  # Draw right branch

        if random.randint(0, 100) < branch_chance:  # Check if a branch should occur
            fork_x = random.randint(min(start_x, end_x), max(start_x, end_x))  # Random fork x-coordinate within valid range
            fork_y = random.randint(min(start_y, end_y), max(start_y, end_y))  # Random fork y-coordinate within valid range
            self.draw_branching_lightning(mid_x, mid_y, fork_x, fork_y, color, depth - 2, branch_chance, fork_chance)  # Draw a branch from the midpoint

    def generate(self, x, y, depth, c):
        result = [[c, (x,y)]]
        for i in range(depth):
            x = result[0][-1][0] + random.randrange(-20,20)
            y = result[0][-1][1] + random.randrange(2,15)
            result[0].append((x, y))

            if random.randrange(0,100) < 5:
                result.extend(self.generate(x, y, depth-i, c+i))

        return result

    def draw(self):
        self.draw_lightning_bolt()  # Call the draw_lightning_bolt method to draw the lightning bolt effect
        self.screen.blit(self.lightning_surface, (0, 0))  # Draw the lightning surface over the entire screen