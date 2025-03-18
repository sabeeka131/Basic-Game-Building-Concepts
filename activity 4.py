import pygame

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")

WHITE = (255, 255, 255)
RECT_COLOR = (230, 230, 250)
TEXT_COLOR = (0, 0, 0)

font = pygame.font.Font(None, 36)
text_surface = font.render("Hello, Pygame!", True, TEXT_COLOR)

rect_width, rect_height = 100, 50
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, rect_width, rect_height))

    text_x = (screen_width - text_surface.get_width()) // 2
    text_y = (screen_height - text_surface.get_height()) // 2 - 100
    screen.blit(text_surface, (text_x, text_y))

    pygame.display.flip()

pygame.quit()