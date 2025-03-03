import pygame, sys
from pygame.locals import QUIT



class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        # fill will fill the screen with white every frame so no artifacts are left behind by moving objects
        self.screen.fill((255, 255, 255)) # replace me with background img later
        self.clock = pygame.time.Clock() # init clock used to set fps/tick speed at bottom of game loop

    def run(self):
        '''
        Main game loop.
        '''
        pygame.display.set_caption('Flappy Bird')
        # fill will fill the screen with white every frame so no artifacts are left behind by moving objects
        self.screen.fill((255, 255, 255)) # replace me with background img later
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

Game().run()
