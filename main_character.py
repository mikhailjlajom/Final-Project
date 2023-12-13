# main_character.py
import pygame

class MainCharacter:
    def __init__(self, screen, floor_tile_map):
        self.screen = screen
        self.floor_tile_map = floor_tile_map
        self.sprite_sheet = pygame.image.load("game_sprites/main_char03_walk.png")
        self.frame_width = self.sprite_sheet.get_width() // 3  # Assuming 3 columns
        self.frame_height = self.sprite_sheet.get_height() // 4  # Assuming 4 rows
        self.frame_count = 12
        self.current_frame = 0
        self.animation_speed = 6.0  # Increased animation speed
        self.last_direction = "down"  # Default last direction
        self.rect = pygame.Rect((screen.get_width() / 2, screen.get_height() / 2), (self.frame_width, self.frame_height))
        self.image = None  # Initialize the 'image' attribute
        self.default_image = self.get_default_image()  # Set a default image

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.y > 0 and self.can_move(self.rect.x, self.rect.y - 300 * dt):
            self.animate("up", dt)
            self.rect.y -= 300 * dt
            self.last_direction = "up"
        elif keys[pygame.K_s] and self.rect.y < self.screen.get_height() - self.frame_height and self.can_move(self.rect.x, self.rect.y + 300 * dt):
            self.animate("down", dt)
            self.rect.y += 300 * dt
            self.last_direction = "down"
        elif keys[pygame.K_a] and self.rect.x > 0 and self.can_move(self.rect.x - 300 * dt, self.rect.y):
            self.animate("left", dt)
            self.rect.x -= 300 * dt
            self.last_direction = "left"
        elif keys[pygame.K_d] and self.rect.x < self.screen.get_width() - self.frame_width and self.can_move(self.rect.x + 300 * dt, self.rect.y):
            self.animate("right", dt)
            self.rect.x += 300 * dt
            self.last_direction = "right"
        else:
            self.image = self.get_default_image(self.last_direction)

    def animate(self, direction, dt):
        self.current_frame += self.animation_speed * dt
        if self.current_frame >= self.frame_count:
            self.current_frame = 0

        frame_x = int(self.current_frame % 3) * self.frame_width
        frame_y = 0  # Start with the first row

        if direction == "up":
            frame_y = 0 * self.frame_height
        elif direction == "right":
            frame_y = 1 * self.frame_height
        elif direction == "down":
            frame_y = 2 * self.frame_height
        elif direction == "left":
            frame_y = 3 * self.frame_height

        self.rect.width = self.frame_width
        self.rect.height = self.frame_height
        self.image = self.sprite_sheet.subsurface(pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height))

    def draw(self):
        if self.image is not None:
            self.screen.blit(self.image, self.rect)

    def get_default_image(self, direction=None):
        frame_x = 1 * self.frame_width
        frame_y = 0  # Start with the first row

        if direction == "up":
            frame_y = 0 * self.frame_height
        elif direction == "right":
            frame_y = 1 * self.frame_height
        elif direction == "down":
            frame_y = 2 * self.frame_height
        elif direction == "left":
            frame_y = 3 * self.frame_height

        default_image = self.sprite_sheet.subsurface(pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height))
        return default_image

# Inside the MainCharacter class
    def can_move(self, x, y):
    # Ensure the character stays within the screen boundaries
        if 0 <= x < self.screen.get_width() - self.frame_width and 0 <= y < self.screen.get_height() - self.frame_height:
            return True

        return False

