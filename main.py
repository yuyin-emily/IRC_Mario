import pygame
import datetime

import bricks

pygame.init()
pygame.display.set_caption("Mario")
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()
clock.tick(55)
background = pygame.image.load("./image/background.png")

running = True

brick = []
for i in range(24): #24塊地板
        brick.append(bricks.bricks(i))

while running:
    time = datetime.datetime.now().second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #print(time)
    
    for i in range(5):
        screen.blit(background,[i * 160,0])
        
    for i in range(24):
        screen.blit(brick[i].img,brick[i].position)
    

    pygame.display.update()

