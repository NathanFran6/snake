from pygame import *

pygame.init()

#ScreenXandY
Screenwid= 500
Screenht=500

#Screen is the win
win = pygame.display.set_mode((Screenwid, Screenh))

#Title and Icon
pygame.display.set_caption('Snake')

#Frame rate
clock= pygame.time.Clock()

def drawWin():
    win.blit(bg,(0,0))

def gameLoop():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        drawWin()


gameLoop()
pygame.quit()