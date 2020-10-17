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
        self.x_change=0
        self.y_change=0
        self.length=1

snakeBlock=10
snakeMulti=[]

def multiSnake(snakeBlock, snakeMulti):
    for x in snakeMulti:
        pygame.draw.rect(win, (0,128,0), [x[0], x[1], snakeBlock, snakeBlock])

 

class food(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=10
        self.height=10
    def score(self):
        if slither.x == self.x and slither.y == self.y:
            slither.length += 1
            self.x=round(random.randrange(0, Screenwid - snakeBlock) / 10.0) * 10.0 
            self.y=round(random.randrange(0, Screenwid - snakeBlock) / 10.0) * 10.0

def boundary():
    if slither.x== 0 or slither.x == Screenwid:
        gameEnd()
    elif slither.y==0 or slither.y== Screenh:
        gameEnd()



def gameEnd():
    end=True
    while end:
        #To mkae the start screen go away
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.fill((0,128,0))
        endText=pygame.font.SysFont('courier',65,True,False)
        endGame= endText.render('Game', 1, (255,255,255))
        win.blit(endGame,(75,70))
        endText2=pygame.font.SysFont('courier',65,True,False)
        endGame2= endText2.render('Over', 1, (255,255,255))
        win.blit(endGame2,(75,155))
        
        pygame.display.update()
        clock.tick(15)

global slither
slither=snake(Screenwid/2,Screenh/2)

global apple
apple=food(round(random.randrange(0, Screenwid - snakeBlock) / 10.0) * 10, 
            round(random.randrange(0, Screenwid - snakeBlock) / 10.0) * 10.0)


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
        win.fill((255,255,255))
        snakeHead=[]
        snakeHead.append(slither.x)
        snakeHead.append(slither.y)
        snakeMulti.append(snakeHead)
        if len(snakeMulti)> slither.length:
            del snakeMulti[0]

        for x in snakeMulti[:-1]:
            if x == snakeHead:
                gameEnd()
        
        slither.x += slither.x_change
        slither.y += slither.y_change
        multiSnake(snakeBlock, snakeMulti)
        pygame.draw.rect(win,(0,128,0),[slither.x, slither.y, snakeBlock, snakeBlock])
        pygame.draw.rect(win,(0,0,0),[apple.x,apple.y,snakeBlock, snakeBlock])
        apple.score()
        boundary()
        pygame.display.update() 
        clock.tick(15)


gameLoop()
pygame.quit()