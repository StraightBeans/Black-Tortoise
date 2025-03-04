# Main game loop
def main():
    bird = Bird()
    pipes = []
    pipe_frequency = 1500  # Pipe frequency in milliseconds
    last_pipe_time = pygame.time.get_ticks()
    score = 0
    game_over = False

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.jump()
                if event.key == pygame.K_SPACE and game_over:
                    # Reset the game if game is over
                    bird = Bird()
                    pipes = []
                    score = 0
                    game_over = False

        # Update the game state only if not game over
        if not game_over:
            # Check for pipe spawning
            current_time = pygame.time.
