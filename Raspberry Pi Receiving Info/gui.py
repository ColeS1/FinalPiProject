import pygame

# initialize Pygame
pygame.init()

# define the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Numbered row_numbers")

# define the font and font size
font = pygame.font.Font(None, 36)

# define the row_numbers of text
row_numbers = ["1", "2", "3", "4", "5"]

strings_representing_functions = ["forward", "backwards"]

# loop through the row_numbers and display them on the screen
for i, row in enumerate(row_numbers):
    # create a text surface
    text_surface = font.render(row, True, pygame.Color("white"))

    # create a rectangle to position the text on the screen
    text_rect = text_surface.get_rect()
    
    
    text_rect.center = (WINDOW_WIDTH // 3, (i + 1) * 50)

    # draw the text surface on the screen
    screen.blit(text_surface, text_rect)

for i, row in enumerate(strings_representing_functions):
    # create a text surface
    text_surface = font.render(row, True, pygame.Color("white"))

    # create a rectangle to position the text on the screen
    text_rect = text_surface.get_rect()

    # divides the window width by 3 and multiplies it by 2 so that it gets put into the center
    text_rect.center = ((WINDOW_WIDTH // 3) * 2, (i + 1) * 50)

    # draw the text surface on the screen
    screen.blit(text_surface, text_rect)



# update the screen
pygame.display.flip()

# run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    i

# quit Pygame
pygame.quit()
