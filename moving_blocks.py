import pygame, sys, time
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Animation")

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
blocks = [b1, b2, b3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(BLACK)

    for b in blocks:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED

        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(0.02)