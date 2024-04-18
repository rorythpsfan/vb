import pygame
import sys
import random
import math
import imageController as IC
class BubbleAnimation:
    def __init__(self, bubble_color):
        pygame.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bubble Animation")

        self.bubbles = []  # Store information about each bubble (x, y, radius, color)

        # Use the specified color for all bubbles
        self.bubble_color = bubble_color

    def create_bubble(self):
        # Place bubbles only within the collision rectangle
        rect_left = (self.width - 100) // 2
        rect_right = rect_left + 100
        rect_top = (self.height - 10) // 2
        rect_bottom = rect_top + 10

        x = random.randint(rect_left, rect_right)
        y = random.randint(rect_top, rect_bottom)
        radius = random.randint(1, 7)  # You can adjust the radius range as needed

        self.bubbles.append((x, y, radius, self.bubble_color))

    def pop(self, index):
        # Get information about the popped bubble
        x, y, radius, color = self.bubbles[index]

        # Add your additional effects when a bubble pops here
        print(f"Bubble popped at index {index}")

        # Remove the bubble that popped
        self.bubbles.pop(index)

    # Create a new bubble with the specified color
        self.create_bubble()



    def draw_bubble(self, x, y, radius, color):
        #self.screen.blit(IC)
        # Draw the bubble on the specified surface
        bubble_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(bubble_surface, color, (radius, radius), radius)

        return bubble_surface

    def check_collision(self, x, y, radius):
        rect_left = (self.width - 100) // 2
        rect_right = rect_left + 100
        rect_top = (self.height - 10) // 2
        rect_bottom = rect_top + 10

        return (
            x - radius < rect_left or
            x + radius > rect_right or
            y - radius < rect_top or
            y + radius > rect_bottom
        )

    def animate_bubbles(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update bubble radius to make them look like they are expanding
            for i in range(len(self.bubbles)):
                x, y, radius, color = self.bubbles[i]
                radius += 0.05  # Adjust the expansion speed as needed
                self.bubbles[i] = (x, y, radius, color)

                # Check if the bubble has touched the edges of the rectangle
                if self.check_collision(x, y, radius):
                    # Call the pop method when a bubble touches the edges
                    self.pop(i)

            # Draw bubbles on the screen
            self.screen.fill((5, 5, 5))  # Fill the screen with a white background

            for x, y, radius, color in self.bubbles:
                # Make the circles transparent and use the specified color
                bubble_surface = self.draw_bubble(x, y, radius, color)
                self.screen.blit(bubble_surface, (x - radius, y - radius))

            pygame.display.flip()

            # Cap the frame rate (adjust as needed)
            clock.tick(30)

    def run(self):
        # Create a specified number of initial bubbles with the specified color
        initial_bubble_count = 5
        for _ in range(initial_bubble_count):
            self.create_bubble()

        # Run the animation loop
        self.animate_bubbles()

if __name__ == "__main__":
    # Specify the color for all bubbles when creating an instance of the class
    bubble_color = (0, 128, 0, 128)  # Green with an alpha value of 128
    bubble_animation = BubbleAnimation(bubble_color)
    bubble_animation.run()
