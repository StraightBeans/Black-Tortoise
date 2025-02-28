import pygame, sys
from pygame.locals import QUIT

# File will contain main game loop, camera, spawning, rendering (some rendering will come from utils file)

class Game():
    def __init__(self):
        pygame.init()


        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        def run(self):
            pygame.display.set_caption('Flappy Bird')
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
                self.clock.tick(60)
