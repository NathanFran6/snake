import pygame

import time

pygame.init()

#ScreenXandY
Screenwid= 710
Screenh=500

#Screen is the win
win = pygame.display.set_mode((Screenwid, Screenh))

#Title and Icon
pygame.display.set_caption('Snake')

#Frame rate
clock= pygame.time.Clock()

#Background
bg=pygame.image.load('C:\\Users\\18597\\Desktop\\My Python Scripts\\snake\\board.png')

#snake class
class snake(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.score=0
        self.block=50

    def draw(self,win):
        pygame.draw.rect(win,(0,128,0),(self.x, self.y, 34,34))


def drawWin():
    win.blit(bg,(0,0))
    slither.draw(win)
    pygame.display.update()
    clock.tick(15)
def gameLoop():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        global slither
        slither=snake(318,253)
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            slither.x= -slither.block
        
        if keys[pygame.K_RIGHT]:
            slither.x+=1

        if keys[pygame.K_UP]:
            slither.y-=1

        if keys[pygame.K_DOWN]:
            slither.y+=1
        drawWin()


gameLoop()
pygame.quit()