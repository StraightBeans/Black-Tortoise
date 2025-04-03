import pygame
import sys
from pygame.locals import QUIT
from entities import Player  # Import the Player class
from pipe import Pipes       # Import the Pipes class from pipe.py
from playscreen import PlayScreen  # Import the PlayScreen class
from background import BACKGROUND_COLOR  # Import background color
from collisions import Collisions

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 640, 480
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True  # Track game state
        self.play_screen = PlayScreen(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.play_screen.show()
        self.start_game()

        # score varible refrenced in game loop
        self.score = 0
        # font for QOL to use later ex can be seen in game loop
        self.font = pygame.font.Font(None, 30)

    def start_game(self):
        """Initialize the game entities."""
        self.running = True
        self.player = Player(self, (100, 100), (34, 24))
        self.pipes = Pipes(speed=-3, screen_width=self.SCREEN_WIDTH, screen_height=self.SCREEN_HEIGHT)
        self.collisions = Collisions(self)

    def run(self):
        pygame.display.set_caption('Flappy Bird')
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.running:
                        self.player.jump()
                    elif event.key == pygame.K_r and not self.running:
                        self.start_game()  # Restart on 'R' press

            if self.running:
                self.screen.fill(BACKGROUND_COLOR)
                self.player.update()
                self.player.render(self.screen)
                self.pipes.update()
                self.pipes.render(self.screen)
                self.collisions.check_screen_collision(self.player)
                self.collisions.check_pipe_collision(self.player, self.pipes)
            else:
                self.display_game_over()

            # Add to score each frame
            self.score += 0.01
            # render score
            score_text = self.font.render(f"Score: {int(self.score)}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))
            
            pygame.display.update()
            self.clock.tick(60)

    def display_game_over(self):
        """Display a Game Over screen."""
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press 'R' to restart", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)


Game().run()
