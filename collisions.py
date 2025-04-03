import pygame

class Collisions:
    def __init__(self, game):
        self.game = game

    def check_screen_collision(self, player):
        """ Check if the player collides with the top or bottom of the screen. """
        if player.pos[1] <= 0:
            player.pos[1] = 0
            player.velocity = 0
            player.game_over()

        if player.pos[1] + player.size[1] >= self.game.SCREEN_HEIGHT:
            player.pos[1] = self.game.SCREEN_HEIGHT - player.size[1]
            player.velocity = 0
            player.game_over()

    def check_pipe_collision(self, player, pipes):
        """ Check if the player collides with any pipes using masks for precise detection. """
        player_mask = pygame.mask.from_surface(player.image)
        player_offset = (int(player.pos[0]), int(player.pos[1]))

        for pipe in pipes.pipes:
            bottom_pipe_mask = pygame.mask.from_surface(pipe.image)
            bottom_offset = (int(pipe.pos[0]), int(pipe.pos[1]))
            top_pipe_mask = pygame.mask.from_surface(pygame.transform.flip(pipe.image, False, True))
            top_offset = (int(pipe.pos[0]), int(pipe.pos[1] - pipe.gap - pipe.image.get_height()))

            # Check for pixel-perfect collision
            if (bottom_pipe_mask.overlap(player_mask, (player_offset[0] - bottom_offset[0], player_offset[1] - bottom_offset[1])) or
                top_pipe_mask.overlap(player_mask, (player_offset[0] - top_offset[0], player_offset[1] - top_offset[1]))):
                player.game_over()
