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

#Movement chnage of the snake

#snake class
class snake(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=10
        self.height=10
        self.score=0
        self.x_change=0
        self.y_change=0


#Background Color
win.fill((255,255,255))
 
global slither
slither=snake(318,253)


def gameLoop():
    run=True
    while run:
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    slither.x_change= -10
                    slither.y_change= 0
            
                if pygame.key==pygame.K_RIGHT:
                    slither.x_change= 10
                    slither.y_change= 0

                if pygame.key==pygame.K_UP:
                    slither.x_change= 0
                    slither.y_change= -10

                if pygame.key==pygame.K_DOWN:
                    slither.x_change= 0
                    slither.y_change= 10

        slither.x += slither.x_change
        slither.y += slither.y_change
        pygame.draw.rect(win,(0,128,0),[slither.x, slither.y, slither.width, slither.height])
        pygame.display.update()
        clock.tick(30)



gameLoop()
pygame.quit()