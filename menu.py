import pygame
import subprocess
import sys
import constants as C
import imageController as IC
import soundManager

class Menu:
    def __init__(self):
        pygame.init()
        self.cycle = [pygame.transform.scale(image, (C.SCREENWIDTH, C.SCREENHEIGHT)) for image in IC.menuBackground]
        self.index = 0
        self.maxIndex = len(self.cycle)
        self.animationCounter = 0
        self.menu_options = ["Continue", "New Game", "Load Game", "Settings", "Extras", "Quit"]
        self.font_size = 30
        self.font_color = (57, 255, 20)
        self.menu_x, self.menu_y = 450, 450
        self.menu_spacing = 40
        self.screen = C.SCREEN
        self.selected_option = 0
        self.animation_frame = 0
        self.frame_delay = 200
        self.clock = pygame.time.Clock()
        self.font_path = "assets/fonts/retro.ttf"
        self.font = pygame.font.Font(self.font_path, self.font_size)
        self.controlsCycle = IC.loadCycle("assets/animations/menu/controls")
        self.flashing_rect_color = self.font_color
        self.flashing_rect_size = (15, 25)
        self.flashing_rect_speed = 10
        self.flashing_rect_pos_y = self.menu_y  # Initial position Y
        self.flashing_rect_visible = True
        self.flashing_rect_timer = 0
        self.flashing_rect_delay = 300  # Milliseconds between each flash
        
        pygame.mixer.music.load(soundManager.songNumber[2])#.wav or .ogg
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(1)

    def draw(self):
        self.screen.blit(self.cycle[self.animation_frame], (0, 0))
        for i, option in enumerate(self.menu_options):
            text_surface = self.font.render(option, True, self.font_color)
            text_rect = text_surface.get_rect(topleft=(self.menu_x, self.menu_y + i * self.menu_spacing))  # Left-aligned
            self.screen.blit(text_surface, text_rect)
        if self.flashing_rect_visible:
            flashing_rect_pos_x = self.menu_x - self.flashing_rect_size[0] - 5  # Position to the left of the menu options
            flashing_rect_pos = (flashing_rect_pos_x, self.flashing_rect_pos_y)
            pygame.draw.rect(self.screen, self.flashing_rect_color, (*flashing_rect_pos, *self.flashing_rect_size))

    def update(self, dt):
        self.flashing_rect_timer += dt
        if self.flashing_rect_timer >= self.flashing_rect_delay:
            self.flashing_rect_timer = 0
            self.flashing_rect_visible = not self.flashing_rect_visible

        self.animationCounter += dt  # Increment animation counter by delta time
        if self.animationCounter >= self.frame_delay:
            self.animation_frame = (self.animation_frame + 1) % len(self.cycle)  # Check if enough time has passed for next frame
            self.animationCounter = 0  # Reset animation counter

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    self.flashing_rect_pos_y = self.menu_y + self.selected_option * self.menu_spacing
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    self.flashing_rect_pos_y = self.menu_y + self.selected_option * self.menu_spacing
                elif event.key == pygame.K_RETURN:
                    selected_option_text = self.menu_options[self.selected_option]
                    if selected_option_text == "Continue":
                        # Continue selected, implement continuation logic
                        pass
                    elif selected_option_text == "New Game":
                    # New Game selected, start a new game by running main.py
                        subprocess.run(["python", "main.py"])
                        sys.exit()  # Exit menu.py to start the game
                    elif selected_option_text == "Load Game":
                    # Load Game selected, implement load game logic
                        pass
                    elif selected_option_text == "Settings":
                    # Settings selected, implement settings menu logic
                        self.menu_options = ["Graphics","Controls", "Audio", "Main Menu"]
                        self.selected_option = 0  # Reset selected option to the first one
                    # Handle other options...
                    elif selected_option_text == "Extras":
                    # Extras
                        self.menu_options = ["Mini Games", "Credits", "Main Menu", "Quit"]
                        self.selected_option = 0  # Reset selected option to the first one
                    # Handle other options...
                    elif selected_option_text == "Graphics":
                        self.menu_options = ["Resolution", "Fullscreen", "Main Menu", "Quit"]
                    elif selected_option_text == "Controls":
                        C.SCREEN.blit(self.controlsCycle[self.animation_frame], (500, 500))
                        self.animationCounter = 0  # Reset animation counter
                    elif selected_option_text == "Audio":
                        self.menu_options = ["Volume +", "Volume -","Mute", "Main Menu", "Quit"]
                    elif selected_option_text == "Main Menu":
                        self.menu_options = ["Continue", "New Game", "Load Game", "Settings", "Extras", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Mini Games":
                        self.menu_options = ["Dragon Poker", "Whack a Mole", "Brain Tetris", "Slide Puzzle", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Credits":
                        pass
                    elif selected_option_text == "Dragon Poker":
                        subprocess.run(["python", "pokey/eyepoker.py"])
                        sys.exit()
                    elif selected_option_text == "Whack a Mole":
                        pass
                    elif selected_option_text == "Brain Tetris":
                        subprocess.run(["python", "brainTetris.py"])
                        sys.exit()
                    elif selected_option_text == "Slide Puzzle":
                        subprocess.run(["python", "slidepuzzle.py"])
                        sys.exit()
                    elif selected_option_text == "Volume +":
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)  # Increase volume
                    elif selected_option_text == "Volume -":
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)  # Decrease volume
                    elif selected_option_text == "Mute":
                        pygame.mixer.music.set_volume(0)  # Mute volume
                    elif selected_option_text == "Resolution":
                        self.menu_options = ["1920x1080", "1600x900", "1280x720", "Full Screen" "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "1920x1080":
                        C.SCREEN = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                        self.menu_options = ["Resolution", "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "1600x900":
                        C.SCREEN = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
                        self.menu_options = ["Resolution", "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "1280x720":
                        C.SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                        self.menu_options = ["Resolution","Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Fullscreen":
                        C.SCREEN = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                        self.menu_options = ["Resolution", "Main Menu", "Quit"]
                        self.selected_option = 0
                    elif selected_option_text == "Quit":
                        pygame.quit()
                        sys.exit()



    def main(self):
        running = True
        last_frame_time = pygame.time.get_ticks()

        while running:
            current_time = pygame.time.get_ticks()
            dt = current_time - last_frame_time
            last_frame_time = current_time

            
            self.draw()
            self.update(dt)

            pygame.display.flip()

if __name__ == "__main__":
    menu = Menu()
    menu.main()
