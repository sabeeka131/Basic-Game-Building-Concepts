import pygame

pygame.init()
#create the display surface object o specific dimension.
window = pygame.display.set_mode((400, 400))
#fill the screen with white color
window.fill((255, 255, 255))
#define colors
GREEN = (152, 251, 152)
#draw solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)
#draw outlined circle
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
#draws the surface object to the screen.
pygame.display.update()
#game loop
running = True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#Quit pygame
pygame.quit()