import pygame, sys
from pygame.locals import QUIT
from entities import Player  # Import the Player class

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        # Create a player instance with starting position and size
        self.player = Player(self, (100, 100), (34, 24))

    def run(self):
        pygame.display.set_caption('Flappy Bird')
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # Input handeling (probably just jump)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # Clear the screen (replace with background later)
            self.screen.fill((255, 255, 255))
            # Update and render the player (funcs from enetities.py)
            self.player.update()
            self.player.render(self.screen) # render player onto self.screen
            pygame.display.update()
            self.clock.tick(60) # FPS max

Game().run()
