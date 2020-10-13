import pygame

import time

import random

pygame.init()

#ScreenXandY
Screenwid= 300
Screenh=300

#List of possible locatons for food
appleX=[10,50,100,150,200,250]
appleY=[10,50,100,150,200,250]

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


class food(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=10
        self.height=10
    def score(self):
        if slither.x== self.x-10 <= self.x <= self.x+10 and slither.y ==  self.y-10<=self.y<=self.y+10:
            slither.score= +1
            self.x= random.choice(appleX)
            self.y= random.choice(appleY)
            print(slither.score)
    def draw(self,win):
        pygame.draw.rect(win,(0,0,0),[self.x,self.y,self.width,self.height])
 
global slither
slither=snake(Screenwid/2,Screenh/2)

apple=food(270,260)


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
            
                if event.key==pygame.K_RIGHT:
                    slither.x_change= 10
                    slither.y_change= 0

                if event.key==pygame.K_UP:
                    slither.x_change= 0
                    slither.y_change= -10

                if event.key==pygame.K_DOWN:
                    slither.x_change= 0
                    slither.y_change= 10

        slither.x += slither.x_change
        slither.y += slither.y_change
        win.fill((255,255,255))
        pygame.draw.rect(win,(0,128,0),[slither.x, slither.y, slither.width, slither.height])
        apple.draw(win)
        apple.score()
        pygame.display.update()
        clock.tick(15)



gameLoop()
pygame.quit()