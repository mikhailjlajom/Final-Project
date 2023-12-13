# story.py
import pygame

intro_done = False
intro_transition_done = False  # New flag for transition
intro_start_time = 0
intro_displayed = False  # Flag to track whether intro has been displayed

def show_intro(screen):
    global intro_done, intro_transition_done, intro_start_time, intro_displayed

    if intro_displayed:
        return

    intro_text = [
        "Welcome to the Way Back Up!",
        "You are assigned to investigate an abandoned house",
        "As you walk to the house and go up the stairs",
        "You press the doorbell and a trapdoor under you opens",
        "you fall"
        # Add more lines as needed
    ]

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text_y = background.get_rect().centery - len(intro_text) * 20

    for line in intro_text:
        partial_line = ""
        for char in line:
            partial_line += char
            text = font.render(partial_line, True, (10, 10, 10))
            textpos = text.get_rect(center=(background.get_rect().centerx, text_y))
            background.fill((250, 250, 250))
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            pygame.time.delay(50)  # Adjust the delay for typing speed

        text_y += 40  # Adjust the vertical spacing between lines
        pygame.time.delay(1000)  # Pause between lines, adjust as needed

    # Update intro_start_time after the intro is done
    intro_start_time = pygame.time.get_ticks()
    intro_done = True
    intro_displayed = True

def set_intro_done(value):
    global intro_done
    intro_done = value

def is_intro_done():
    global intro_done
    return intro_done

def set_intro_transition_done(value):
    global intro_transition_done
    intro_transition_done = value

def is_intro_transition_done():
    global intro_transition_done
    return intro_transition_done

def get_intro_start_time():  
    global intro_start_time
    return intro_start_time

def set_intro_start_time(value):  
    global intro_start_time
    intro_start_time = value
