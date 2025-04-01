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
        """ Check if the player collides with any pipes. """
        player_rect = player.rect()

        for pipe in pipes.pipes:  # Access the pipes list from Pipes class
            # Create rects for top and bottom pipes
            bottom_pipe = pygame.Rect(pipe.pos[0], pipe.pos[1], pipe.pipe_width, pipe.image.get_height())
            top_pipe = pygame.Rect(pipe.pos[0], pipe.pos[1] - pipe.gap - pipe.image.get_height(), 
                                 pipe.pipe_width, pipe.image.get_height())
            
            # Check collision with either pipe
            if player_rect.colliderect(bottom_pipe) or player_rect.colliderect(top_pipe):
                player.game_over()
