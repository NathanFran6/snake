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
        self.score=0
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
    if slither.x== 0 or slither.x == Screenwid-10:
        print('Game Over')
    elif slither.y==0 or slither.y== Screenh-10:
        print('Game Over')

def gameEnd():
    end=True
    while end:
        #To mkae the start screen go away
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.fill((255,255,255))
        endText=pygame.font.SysFont('goudystout',30,True,False)
        endGame= endText.render('Game', 1, (255,255,255))
        win.blit(endGame,(90,90))
        endText2=pygame.font.SysFont('goudystout',30,True,False)
        endGame2= endText2.render('Game Over', 1, (255,255,255))
        win.blit(endGame2,(60,150))
        
        button('Play Again',170,190,180,50,startButton2,startButton,215,205,textColor2,textColor,'play')
        
        pygame.display.update()
        clock.tick(15)

def endButton(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'play':
                    gameLoop()
        else:       
            pygame.draw.rect(win, active,(x,y,w,h))

        buttonText= pygame.font.SysFont('goudystout',15,False,False)
        buttonType= buttonText.render(msg,1,(activeT))
        buttonText2= pygame.font.SysFont('goudystout',15,False,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))
        if x+w> mouse[0] >x and y+h>mouse[1] > y:
            win.blit(buttonType2,(xT,yT))
        else:
            win.blit(buttonType,(xT,yT))            
        buttonText2= pygame.font.SysFont('goudystout',15,False,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))

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
        snakeHead=[]
        snakeHead.append(slither.x)
        snakeHead.append(slither.y)
        snakeMulti.append(snakeHead)
        if len(snakeMulti)> slither.length:
            del snakeMulti[0]

        for x in snakeMulti[:-1]:
            if x == snakeHead:
                print('Game Over')
        
        slither.x += slither.x_change
        slither.y += slither.y_change
        win.fill((255,255,255))
        multiSnake(snakeBlock, snakeMulti)
        pygame.draw.rect(win,(0,128,0),[slither.x, slither.y, snakeBlock, snakeBlock])
        pygame.draw.rect(win,(0,0,0),[apple.x,apple.y,snakeBlock, snakeBlock])
        apple.score()
        boundary()
        pygame.display.update() 
        clock.tick(15)


gameEnd()
pygame.quit()