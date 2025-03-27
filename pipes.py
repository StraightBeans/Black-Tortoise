import pygame
import random

class Pipe:
    def __init__(self, pos, speed, gap, screen_height, pipe_width=130):  # Increased width from 80 to 130
        self.pos = list(pos)
        self.speed = speed
        self.gap = gap + 20  # Slightly increase the gap for better playability
        self.screen_height = screen_height
        self.pipe_width = pipe_width

                # Load the pipe image and scale it
        self.image = pygame.image.load("pipe image.png")
        self.image = pygame.transform.scale(self.image, (self.pipe_width, int(self.screen_height * 0.7)))  # Increase pipe height

    def update(self):
        self.pos[0] += self.speed
        
    def render(self, surf):
            # Draw the bottom pipe
        surf.blit(self.image, (self.pos[0], self.pos[1]))

            # Flip the image for the top pipe and position it correctly
        flipped_pipe = pygame.transform.flip(self.image, False, True)
        surf.blit(flipped_pipe, (self.pos[0], self.pos[1] - self.gap - self.image.get_height()))

class Pipes:
    def __init__(self, speed, screen_width, screen_height, gap=110, frequency=750, pipe_width=180):
        """
        speed: Horizontal movement speed for the pipes.
        screen_width, screen_height: Dimensions of the game screen.
        gap: Vertical gap between the top and bottom pipes.
        frequency: Time interval (in milliseconds) between spawning new pipes.
        pipe_width: The width of the pipes.
        """
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.gap = gap
        self.frequency = frequency
        self.pipe_width = pipe_width
        self.pipes = []
        self.last_pipe_time = pygame.time.get_ticks()

    def update(self):
        # Update the position of each pipe.
        for pipe in self.pipes:
            pipe.update()

        # Remove pipes that have completely scrolled offscreen.
        self.pipes = [pipe for pipe in self.pipes if pipe.pos[0] + self.pipe_width > 0]

        # Check if it's time to spawn a new pipe pair.
        current_time = pygame.time.get_ticks()
        if current_time - self.last_pipe_time > self.frequency:
            # Determine a random vertical position for the gap.
            # Ensuring that there is a minimum height for the top and bottom pipes.
            min_gap_y = self.gap + 50  # Top pipe will have at least 50 pixels.
            max_gap_y = self.screen_height - 50  # Bottom pipe will have at least 50 pixels.
            gap_y = random.randint(min_gap_y, max_gap_y)

            # Create a new pipe pair at the right edge of the screen.
            new_pipe = Pipe(pos=(self.screen_width, gap_y), speed=self.speed, gap=self.gap,
                            screen_height=self.screen_height, pipe_width=self.pipe_width)
            self.pipes.append(new_pipe)
            self.last_pipe_time = current_time

    def render(self, surf):
        # Render all pipe pairs.
        for pipe in self.pipes:
            pipe.render(surf)
