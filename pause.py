import pygame

class PauseMenu:
    def __init__(self, screen, text_color):
        self.screen = screen
        self.text_color = text_color

    def update(self):
        # Pause menu logic and rendering when paused
        font = pygame.font.Font(None, 100)
        text = font.render("Paused - Press 'P' to resume", True, self.text_color)
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
