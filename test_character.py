import pygame
from main_character import MainCharacter

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

character = MainCharacter(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000
    character.update(dt)

    screen.fill((255, 255, 255))  # Fill the screen with white color
    character.draw()

    pygame.display.flip()

pygame.quit()
