import pygame
from random import randint
pygame.init()


LEFT_BUTTON = 1
WINDOW_SIZE = (640, 480)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
x = 50

running = True

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BLACK)


rect_list = []
rect_list.append(pygame.Rect(10, 240, 100, 100))
rect_list.append(pygame.Rect(140, 240, 100, 100))
rect_list.append(pygame.Rect(270, 240, 100, 100))
rect_list.append(pygame.Rect(400, 240, 100, 100))
rect_list.append(pygame.Rect(530, 240, 100, 100))
my_font = pygame.font.SysFont("Comic Sans MS", 30)

for box in rect_list:
    pygame.draw.rect(window, RED, box)
    label = my_font.render(str(randint(1,6)), 1, BLUE)
    for box in rect_list:
        window.blit(label, (x, 260))
        x = x =+ 130
        pygame.display.flip()



while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        for box in rect_list:
            if box.collidepoint(event.pos):
                window.fill(BLACK)
                for box in rect_list:
                    pygame.draw.rect(window,RED, box)
                label = my_font.render(str(randint(1,6)), 1, BLUE)
                window.blit(label, (230, 260))

    pygame.display.flip()