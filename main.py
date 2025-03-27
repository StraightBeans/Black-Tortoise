import pygame
import sys
from pygame.locals import QUIT
from entities import Player  # Import the Player class
from pipe import Pipes       # Import the Pipes class from pipe.py
from playscreen import PlayScreen  # Import the PlayScreen class
from background import BACKGROUND_COLOR

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 640, 480
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.score = 0
        self.font = pygame.font.Font(None, 30)

        # Show the play screen before the game starts
        self.play_screen = PlayScreen(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.play_screen.show()

        # Create a player instance with starting position and size
        self.player = Player(self, (100, 100), (34, 24))
        # Instantiate the Pipes class with appropriate parameters
        self.pipes = Pipes(speed=-6, screen_width=self.SCREEN_WIDTH, screen_height=self.SCREEN_HEIGHT)

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

            #Background Color
            self.screen.fill(BACKGROUND_COLOR)
            # Update and render the player
            self.player.update()
            self.player.render(self.screen)

            # Update and render the pipes
            self.pipes.update()
            self.pipes.render(self.screen)

            # Add to score each frame
            self.score += 0.01
            print(int(self.score))
            # render score
            score_text = self.font.render(f"Score: {int(self.score)}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.update()
            self.clock.tick(60)  # Max FPS

Game().run()
