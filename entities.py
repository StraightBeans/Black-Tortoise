import pygame

class Bird:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8
        self.offscreen = False

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        self.velocity += self.gravity
        self.pos[1] += self.velocity
    if self.pos[1] -= self.vol
        # check if offscreen
        rect = self.rect()
        if (rect.right < 0 or rect.left > self.game.SCREEN_WIDTH or
            rect.bottom < 0 or rect.top > self.game.SCREEN_HEIGHT):
            self.offscreen = True
        print("Offscreen = ", self.offscreen)

    def render(self, surf):
        pygame.draw.rect(surf, (255, 255, 0), (self.pos[0], self.pos[1], self.size[0], self.size[1]))


class Player(Bird):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)
        self.jumps = True 
        self.score = 0
    
    def jump(self):
        self.velocity = self.jump_strength
