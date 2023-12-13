# transition_screen.py

import pygame

def show_transition(screen, duration=5000):
    pygame.mixer.music.load("game_sounds/falling_effect.wav")
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()

    # Draw black transition screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Wait for the specified duration
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration:
        clock.tick(60)  # Adjust the frame rate as needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.mixer.music.stop()
