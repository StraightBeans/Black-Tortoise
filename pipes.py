import pygame
import random

class Pipe:
    def __init__(self, pos, speed, gap, screen_height, pipe_width=80):
        """
        pos: A tuple (x, gap_y) where gap_y is the top edge of the bottom pipe.
        speed: Horizontal movement speed (typically negative for leftward movement).
        gap: The vertical gap between the top and bottom pipes.
        screen_height: The height of the game screen.
        pipe_width: The width of the pipes.
        """
        self.pos = list(pos)
        self.speed = speed
        self.gap = gap
        self.screen_height = screen_height
        self.pipe_width = pipe_width

    def update(self):
        # Move the pipe horizontally.
        self.pos[0] += self.speed

    def render(self, surf):
        # Calculate the bottom pipe rectangle:
        # Bottom pipe starts at pos[1] and extends to the bottom of the screen.
        bottom_rect = pygame.Rect(self.pos[0], self.pos[1], self.pipe_width, self.screen_height - self.pos[1])
        
        # Calculate the top pipe rectangle:
        # Top pipe starts at the top of the screen and extends down to (gap_y - gap).
        top_rect = pygame.Rect(self.pos[0], 0, self.pipe_width, self.pos[1] - self.gap)
        
        # Draw both pipes as green rectangles. (replace later)
        pygame.draw.rect(surf, (0, 255, 0), bottom_rect)
        pygame.draw.rect(surf, (0, 255, 0), top_rect)

class Pipes:
    def __init__(self, speed, screen_width, screen_height, gap=150, frequency=1500, pipe_width=80):
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
