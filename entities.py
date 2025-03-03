import pygame 

# needs a Physics_entity class that will have gravity and other applicable things
# player with be a child of that class with jump and other functions in it 

class Bird:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        self.velocity += self.gravity
        self.pos[1] += self.velocity

    def jump(self):
        self.velocity = self.jump_strength

    def render(self, surf, offset=(0, 0)):
        pygame.draw.rect(surf, (255, 255, 0), (self.pos[0] - offset[0], self.pos[1] - offset[1], self.size[0], self.size[1]))

class Player(Bird):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)
        self.jumps = True 
        self.score = 0
