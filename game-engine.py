# game-engine.py
import pygame
import story
from main_character import MainCharacter
from transition_screen import show_transition

pygame.init()
pygame.display.set_caption('Way Back Up')  # Set the window title
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("game_sprites/scene.png")
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))
        self.background_rect = self.background_image.get_rect()

    def draw(self):
        self.screen.blit(self.background_image, self.background_rect)
        font = pygame.font.Font(None, 48)
        title_text = font.render("Way Back Up", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(self.screen.get_width() / 2, 50))
        self.screen.blit(title_text, title_rect)

        # Draw Start Game button
        pygame.draw.rect(self.screen, (0, 128, 255), (self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 - 25, 200, 50), border_radius=10)
        font = pygame.font.Font(None, 36)
        text = font.render("Start Game", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 25 + 25))
        self.screen.blit(text, text_rect)

        # Draw Exit Game button
        pygame.draw.rect(self.screen, (255, 0, 0), (self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 + 25, 200, 50), border_radius=10)
        text = font.render("Exit Game", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 25 + 25))
        self.screen.blit(text, text_rect)

class IntroScreen:
    def __init__(self, screen):
        self.screen = screen
        self.intro_done = False

    def draw(self):
        if not self.intro_done:
            story.show_intro(self.screen)
            self.intro_done = True

class GameScreen:
    def __init__(self, screen, stage_module):
        self.screen = screen
        self.character = MainCharacter(screen, stage_module.get_tile_map())
        self.floor_tile_map = stage_module.get_tile_map()
        self.floor_images = {
            1: pygame.image.load("game_sprites/flooring/bricks.png"),  # Add the path to your default floor image
            2: pygame.image.load("game_sprites/flooring/ice.png")  # Assuming this is the ice floor image
            # Add more mappings for other floor tile types if needed
        }

    def update(self, dt):
        self.character.update(dt)

    def draw(self):
        self.screen.fill((255, 255, 255))  # Fill the screen with white color

        # Draw floor tiles
        self.draw_floor()

        # Draw the main character
        self.character.draw()

    def draw_floor(self):
        tile_size = 32  # Adjust the size of your tiles

        for row in range(len(self.floor_tile_map)):
            for col in range(len(self.floor_tile_map[row])):
                tile_type = self.floor_tile_map[row][col]
                if tile_type in self.floor_images:
                    self.screen.blit(self.floor_images[tile_type], (col * tile_size, row * tile_size))
                # Add more conditions for other tile types

# ...

# Initial screen
current_screen = StartScreen(screen)
intro_screen = IntroScreen(screen)
stage_module = __import__('stage1_floor')  # Import the initial stage module
game_screen = GameScreen(screen, stage_module)
transition_screen = False

# Load opening music on loop
pygame.mixer.music.load("game_sounds/opening_theme.mp3")
pygame.mixer.music.play(-1)

intro_shown = False
game_started = False
transition_start_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            # Check if the Start Game button is clicked
            start_button_rect = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 25, 200, 50)
            exit_button_rect = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 25, 200, 50)

            if start_button_rect.collidepoint(mouse_x, mouse_y) and not intro_shown:
                intro_screen = IntroScreen(screen)
                current_screen = intro_screen
                pygame.mixer.music.stop()
                intro_shown = True
            elif exit_button_rect.collidepoint(mouse_x, mouse_y):
                running = False

        elif event.type == pygame.KEYDOWN:
            # Check if any key is pressed to trigger the game start and stop the music
            if not intro_shown and not transition_screen:
                intro_screen = IntroScreen(screen)
                current_screen = intro_screen
                pygame.mixer.music.stop()
                intro_shown = True

    current_screen.draw()

    if intro_shown and not transition_screen:
        if story.is_intro_done():
            show_transition(screen)
            transition_screen = True
            transition_start_time = pygame.time.get_ticks()
            story.set_intro_done(False)

    if transition_screen:
        if pygame.time.get_ticks() - transition_start_time >= 5000:
            game_screen.update(dt)  # Update the game_screen before checking the transition
            current_screen = game_screen
            game_started = True
            transition_screen = False

    if game_started:
        game_screen.update(dt)
    
    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()