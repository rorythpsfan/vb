import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eye Poker")

# Colors
WHITE = (255, 255, 255)

# Eye class
class Eye(pygame.sprite.Sprite):
    UPGRADE_COST = 1000

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, (255, 165, 0), (50, 50), 50)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.score = 0
        self.upgrade_purchased = False

    def update(self):
        # Check for clicks
        if pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                    self.score += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Upgrade class
class Upgrade:
    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.rect = pygame.Rect(10, 50, 200, 30)

# Define upgrades
upgrades = [
    Upgrade("Upgrade 1", 500, lambda eye: apply_upgrade(eye)),  # Example upgrade 1
    Upgrade("Upgrade 2", 1000, lambda eye: eye.image.fill((0, 255, 0))),  # Example upgrade 2
    # Add more upgrades as needed
]

# Function to apply upgrade
def apply_upgrade(eye):
    if eye.score >= 100:
        eye.UPGRADE_COST -= 100

# Function to draw the upgrades menu
def draw_upgrade_menu(screen):
    font = pygame.font.Font(None, 24)
    y_offset = 50
    for i, upgrade in enumerate(upgrades):
        upgrade_text = f"{upgrade.name} - Cost: {upgrade.cost}"
        text_surface = font.render(upgrade_text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (upgrade.rect.left, upgrade.rect.top + y_offset * i)
        screen.blit(text_surface, text_rect.topleft)

# Function to handle clicking on upgrades
def handle_upgrade_click(eye):
    mouse_pos = pygame.mouse.get_pos()
    for upgrade in upgrades:
        if upgrade.rect.collidepoint(mouse_pos):
            if eye.score >= upgrade.cost:
                upgrade.effect(eye)
                eye.score -= upgrade.cost
                break

# Main function
def main():
    clock = pygame.time.Clock()

    eye = Eye()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(eye)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_upgrade_click(eye)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print ("released mouse button")# Update
        all_sprites.update()

        # Draw everything
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        draw_upgrade_menu(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {eye.score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
