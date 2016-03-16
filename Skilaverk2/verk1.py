import pygame

pygame.init()

# Color constants
WHITE = (255, 255, 255)
BOX_COLOR = (100, 150, 100)


window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

# Box Color
color = BOX_COLOR

# the list to hold all the rectangles
rect_list = []

# loop control variable set to initial value of 0
n = 0

pygame.display.set_caption('Rectangles in a Row')
window.fill(WHITE)


# rectangles with positions added to a list
for n in range(5):
    rect_list.append(pygame.Rect(30 + (n * 70), 30, 60, 60))

# the while-loop control variable set to it's initial value
running = True

# let the games begin :-)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # the rectangles in the rect_list printed out
    for r in rect_list:
        pygame.draw.rect(window, color, r)

    pygame.display.update()

pygame.quit()