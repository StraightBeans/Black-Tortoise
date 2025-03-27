import pygame
from background import BACKGROUND_COLOR

class PlayScreen:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("Flappy Bird", True, (0, 0, 0))
        self.instruction_text = self.font.render("Press SPACE to Start", True, (0, 0, 0))
        self.running = True

    def show(self):
        while self.running:
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.fill((255, 255, 255))  # White background
            self.screen.blit(self.title_text, (self.screen_width // 2 - 50, self.screen_height // 3))
            self.screen.blit(self.instruction_text, (self.screen_width // 2 - 100, self.screen_height // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = False

            pygame.display.update()
