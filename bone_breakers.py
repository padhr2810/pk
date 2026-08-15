#stickMan bone breaking
import pygame,time,random,sys
from pygame.locals import *
pygame.init()
import time


width = 1000
height = 800

window = pygame.display.set_mode((width,height))

pygame.display.set_caption('')

goodCircleCenter = [300,300]
badCircleCenter = [600,600]
red = (200,20,0)
blue = (0,0,255)
while True:
                     
    backroundColour = (134,223,10)
    window.fill(backroundColour)   
     
    
    pygame.draw.circle(window,blue,(goodCircleCenter), 30,0)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                
                goodCircleCenter[1] -= 20
            if event.key == K_DOWN:
                goodCircleCenter[1] += 20
            if event.key == K_RIGHT:
                goodCircleCenter[0] += 20
            if event.key == K_LEFT:
                goodCircleCenter[0] -= 20
                
          
    badCircle1 = pygame.draw.circle(window,red,(badCircleCenter),50,0)
    badCircleCenter2 = [700,700]
    badCircle2 = pygame.draw.circle(window,red,(badCircleCenter2),50,0)
    
    badCircleCenter[0] += (20)   
    pygame.display.update()
