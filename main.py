import pygame, sys
from pygame.locals import QUIT
from entities import Player  # Import the Player class
from pipe import Pipes       # Import the Pipes class from pipe.py

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 640, 480
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        # Create a player instance with starting position and size
        self.player = Player(self, (100, 100), (34, 24))
        # Instantiate the Pipes class with appropriate parameters
        self.pipes = Pipes(speed=-3, screen_width=self.SCREEN_WIDTH, screen_height=self.SCREEN_HEIGHT)
        
    def run(self):
        pygame.display.set_caption('Flappy Bird')
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # Input handling (jump)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # Clear the screen (replace with background later)
            self.screen.fill((255, 255, 255))
            # Update and render the player
            self.player.update()
            self.player.render(self.screen)
            # Update and render the pipes
            self.pipes.update()
            self.pipes.render(self.screen)
            
            pygame.display.update()
            self.clock.tick(60)  # Max FPS

Game().run()
