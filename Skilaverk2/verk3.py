import pygame
pygame.init()
starting_x = 30
starting_y = 30
x = 0
y = 0
COLOR = (255, 255, 255)
screen = pygame.display.set_mode((400, 300))
LEFT_BUTTON = 1
# Access to the clock is necessary for screen speed control
clock = pygame.time.Clock()
frames_per_second = 20
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        x, y = event.pos
        while starting_x != x and starting_y != y:
            starting_x += 1
            starting_y += 1
            screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255,255,0), (starting_x,starting_y), 20,2)

    pygame.display.flip()
    clock.tick(frames_per_second)