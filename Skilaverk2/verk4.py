import pygame

pygame.init()

window_size = window_width,window_height = 640, 480
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

BACKGROUND = (0, 255, 0)

window.fill(BACKGROUND)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


pygame.quit()