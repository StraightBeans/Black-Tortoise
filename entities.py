import pygame

class Bird:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = (int(size[0] * 2), int(size[1] * 2))
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8
        self.offscreen = False
        self.image = pygame.image.load("bird image.png")
        self.image = pygame.transform.scale(self.image, self.size)

    def render(self, surf):
        surf.blit(self.image, (self.pos[0], self.pos[1]))

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        self.velocity += self.gravity
        self.pos[1] += self.velocity
        if self.pos[1] <= 0:
            self.pos[1] = 0
            self.velocity = 0
            self.game_over() 
    def game_over(self):
        print("Game Over! You died")
        self.is_game_over = True
        rect = self.rect()
        if (rect.right < 0 or rect.left > self.game.SCREEN_WIDTH or
        rect.bottom < 0 or rect.top > self.game.SCREEN_HEIGHT):
            self.offscreen = True
        print("Offscreen = ", self.offscreen)


class Player(Bird):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)
        self.jumps = True 
        self.score = 0

    def jump(self):
        self.velocity = self.jump_strength
